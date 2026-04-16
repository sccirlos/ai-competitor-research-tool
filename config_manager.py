"""
Helper functions for managing research focus area configurations
"""
import json
import os
from typing import Dict, List, Optional

CONFIG_FILE = "research_configs.json"

def load_research_configs() -> Dict:
    """Load research configurations from JSON file"""
    if not os.path.exists(CONFIG_FILE):
        # Create default config if it doesn't exist
        default_config = {
            "ai_features": {
                "name": "AI Features & Capabilities",
                "description": "Focus on AI-powered features, automation, and technical innovation",
                "prompt_template": "Default AI-focused prompt...",
                "is_builtin": True
            },
            "groups_services": {
                "name": "Groups & Service Offerings",
                "description": "Focus on group practice features, service capabilities, and insurance",
                "prompt_template": "Default groups-focused prompt...",
                "is_builtin": True
            }
        }
        save_research_configs(default_config)
        return default_config
    
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def save_research_configs(configs: Dict) -> None:
    """Save research configurations to JSON file"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(configs, f, indent=2)

def get_config_names() -> List[str]:
    """Get list of all research focus area names"""
    configs = load_research_configs()
    return [config['name'] for config in configs.values()]

def get_config_by_name(name: str) -> Optional[Dict]:
    """Get a specific config by its display name"""
    configs = load_research_configs()
    for config_id, config in configs.items():
        if config['name'] == name:
            return {"id": config_id, **config}
    return None

def add_research_config(name: str, description: str, prompt_template: str) -> bool:
    """Add a new research configuration"""
    configs = load_research_configs()
    
    # Generate a unique ID (lowercase, underscores)
    config_id = name.lower().replace(' ', '_').replace('&', 'and')
    
    # Check if name already exists
    for config in configs.values():
        if config['name'] == name:
            return False
    
    configs[config_id] = {
        "name": name,
        "description": description,
        "prompt_template": prompt_template,
        "is_builtin": False
    }
    
    save_research_configs(configs)
    return True

def update_research_config(config_id: str, name: str, description: str, prompt_template: str) -> bool:
    """Update an existing research configuration"""
    configs = load_research_configs()
    
    if config_id not in configs:
        return False
    
    configs[config_id]['name'] = name
    configs[config_id]['description'] = description
    configs[config_id]['prompt_template'] = prompt_template
    
    save_research_configs(configs)
    return True

def delete_research_config(config_id: str) -> bool:
    """Delete a research configuration (only custom ones)"""
    configs = load_research_configs()
    
    if config_id not in configs:
        return False
    
    # Don't allow deleting builtin configs
    if configs[config_id].get('is_builtin', False):
        return False
    
    del configs[config_id]
    save_research_configs(configs)
    return True

def get_prompt_for_config(config_name: str, competitor_name: str, competitor_url: str) -> str:
    """Get the formatted prompt for a specific config"""
    config = get_config_by_name(config_name)
    if not config:
        return ""
    
    prompt = config['prompt_template']
    # Replace placeholders
    prompt = prompt.replace('{competitor_name}', competitor_name)
    prompt = prompt.replace('{competitor_url}', competitor_url)
    
    return prompt
