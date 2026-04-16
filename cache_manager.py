"""
Cache management for competitive research data.

Key improvement:
- Cache entries now store and restore a specific output folder path per run,
  instead of assuming all runs for a day live in the same shared folder.

This prevents stale or mixed results when multiple analyses are run on the same day.
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict

CACHE_METADATA_FILE = Path("cache_metadata.json")
CACHE_DURATION_DAYS = 14
CACHE_STORAGE_DIR = Path("cached_outputs")
OUTPUTS_DIR = Path("outputs")


def load_cache_metadata() -> Dict[str, Any]:
    """Load cache metadata from disk."""
    if not CACHE_METADATA_FILE.exists():
        return {}

    try:
        with CACHE_METADATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_cache_metadata(metadata: Dict[str, Any]) -> None:
    """Persist cache metadata to disk."""
    with CACHE_METADATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)


def get_cache_key(competitor_name: str, focus_id: str) -> str:
    """Create a stable cache key for a competitor + focus combination."""
    comp_key = competitor_name.lower().replace(" ", "_")
    focus_key = focus_id.lower().replace(" ", "_")
    return f"{comp_key}_{focus_key}"


def is_cache_valid(last_updated_str: str) -> bool:
    """Return True if the cache entry is still within the retention window."""
    try:
        last_updated = datetime.fromisoformat(last_updated_str)
        return (datetime.now() - last_updated) < timedelta(days=CACHE_DURATION_DAYS)
    except Exception:
        return False


def _copy_directory(source_dir: Path, target_dir: Path) -> None:
    """Replace the target directory with a fresh copy of the source directory."""
    if target_dir.exists():
        shutil.rmtree(target_dir)
    shutil.copytree(source_dir, target_dir)


def save_to_cache(
    competitor_name: str,
    focus_id: str,
    output_folder_name: str,
    *,
    focus_name: str | None = None,
) -> bool:
    """
    Save a specific run's output folder to cache.

    Args:
        competitor_name: Human-readable competitor name.
        focus_id: Stable focus identifier used for cache keying.
        output_folder_name: Folder name inside ./outputs for this exact run.
        focus_name: Optional display name for the focus area.

    Returns:
        True if the cache save succeeded, otherwise False.
    """
    metadata = load_cache_metadata()
    cache_key = get_cache_key(competitor_name, focus_id)

    source_dir = OUTPUTS_DIR / output_folder_name
    if not source_dir.exists() or not source_dir.is_dir():
        return False

    CACHE_STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    cache_folder = CACHE_STORAGE_DIR / cache_key

    try:
        _copy_directory(source_dir, cache_folder)
    except Exception:
        return False

    metadata[cache_key] = {
        "competitor_name": competitor_name,
        "focus_id": focus_id,
        "focus_name": focus_name or focus_id,
        "last_updated": datetime.now().isoformat(),
        "cache_folder": str(cache_folder),
        "output_folder_name": output_folder_name,
    }

    save_cache_metadata(metadata)
    return True


def load_from_cache(cache_key: str, target_folder_name: str) -> bool:
    """
    Restore a cached run into ./outputs/<target_folder_name>.
    """
    metadata = load_cache_metadata()
    if cache_key not in metadata:
        return False

    cache_entry = metadata[cache_key]
    cache_folder = Path(cache_entry.get("cache_folder", ""))

    if not cache_folder.exists() or not cache_folder.is_dir():
        return False

    if not is_cache_valid(cache_entry.get("last_updated", "")):
        return False

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    target_dir = OUTPUTS_DIR / target_folder_name

    try:
        _copy_directory(cache_folder, target_dir)
    except Exception:
        return False

    return True


def clear_old_cache_entries() -> int:
    """Delete expired cache entries and remove their cached folders."""
    metadata = load_cache_metadata()
    keys_to_remove: list[str] = []

    for key, entry in metadata.items():
        last_updated = entry.get("last_updated", "")
        if last_updated and not is_cache_valid(last_updated):
            keys_to_remove.append(key)

            cache_folder = Path(entry.get("cache_folder", ""))
            if cache_folder.exists():
                shutil.rmtree(cache_folder)

    for key in keys_to_remove:
        metadata.pop(key, None)

    if keys_to_remove:
        save_cache_metadata(metadata)

    return len(keys_to_remove)


def format_cache_age(last_updated_str: str) -> str:
    """Return a human-readable age string for a cache entry."""
    try:
        last_updated = datetime.fromisoformat(last_updated_str)
        age = datetime.now() - last_updated

        if age < timedelta(hours=1):
            minutes = max(1, int(age.total_seconds() / 60))
            return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
        if age < timedelta(days=1):
            hours = int(age.total_seconds() / 3600)
            return f"{hours} hour{'s' if hours != 1 else ''} ago"
        if age < timedelta(days=7):
            days = int(age.days)
            return f"{days} day{'s' if days != 1 else ''} ago"

        return last_updated.strftime("%B %d, %Y at %I:%M %p")
    except Exception:
        return "Unknown"


def get_all_cached_items() -> Dict[str, Dict[str, Any]]:
    """
    Return cache entries for UI display, sorted newest first.
    """
    metadata = load_cache_metadata()
    items: list[tuple[str, Dict[str, Any]]] = []

    for key, entry in metadata.items():
        last_updated = entry.get("last_updated")
        focus_name = entry.get("focus_name", "Unknown")

        record = {
            "competitor": entry.get("competitor_name", "Unknown"),
            "focus": focus_name,
            "focus_id": entry.get("focus_id", ""),
            "age": format_cache_age(last_updated) if last_updated else "Unknown",
            "timestamp": last_updated,
            "valid": bool(last_updated and is_cache_valid(last_updated)),
            "output_folder_name": entry.get("output_folder_name", ""),
        }

        if not record["valid"]:
            record["age"] = "Expired"

        items.append((key, record))

    items.sort(key=lambda item: item[1].get("timestamp") or "", reverse=True)
    return dict(items)
