import json
import os
import pandas as pd
from glob import glob
from datetime import datetime


def compile_json_to_csv(
    output_folder_name=None,
    focus_name=None,
    selected_competitors=None
):
    if not output_folder_name:
        output_folder_name = datetime.now().strftime("%Y-%m-%d")

    base_dir = f"outputs/{output_folder_name}"
    raw_dir = f"{base_dir}/raw"
    comp_dir = f"{base_dir}/comparisons"

    if not os.path.exists(raw_dir):
        print(f"Error: Directory {raw_dir} does not exist.")
        return

    all_features = []
    ai_features = []
    branded_solutions = []
    groups_offerings = []
    service_offerings = []
    insurance_offerings = []
    market_intelligence = []

    json_files = glob(os.path.join(raw_dir, "*.json"))

    if selected_competitors:
        selected_lookup = {
            name.lower().replace(" ", "")
            for name in selected_competitors
        }

        json_files = [
            file_path
            for file_path in json_files
            if os.path.basename(file_path)
            .replace(".json", "")
            .lower()
            .replace(" ", "") in selected_lookup
        ]
    # -----------------------------------------------------------------------
    # Phase 1: Raw per-competitor JSON (discover_and_extract outputs)
    # -----------------------------------------------------------------------
    for file_path in json_files:
        competitor_name = os.path.basename(file_path).replace(".json", "").capitalize()
        print(f"Processing {competitor_name}...")

        try:
            with open(file_path, "r") as f:
                data = json.load(f)

            # --- General features ---
            for feat in data.get("all_features", []):
                feat_copy = feat.copy()
                feat_copy["competitor"] = competitor_name
                if isinstance(feat_copy.get("available_in_tiers"), list):
                    feat_copy["available_in_tiers"] = ", ".join(feat_copy["available_in_tiers"])
                all_features.append(feat_copy)

            # --- AI features ---
            for feat in data.get("ai_features", []):
                feat_copy = feat.copy()
                feat_copy["competitor"] = competitor_name
                if isinstance(feat_copy.get("available_in_tiers"), list):
                    feat_copy["available_in_tiers"] = ", ".join(feat_copy["available_in_tiers"])
                ai_features.append(feat_copy)

            # --- Branded solutions ---
            for sol in data.get("branded_solutions", []):
                sol_copy = sol.copy()
                sol_copy["competitor"] = competitor_name
                if isinstance(sol_copy.get("core_capabilities"), list):
                    sol_copy["core_capabilities"] = "; ".join(sol_copy["core_capabilities"])
                branded_solutions.append(sol_copy)

            # --- Groups offerings ---
            for offering in data.get("groups_offerings", []):
                offering_copy = offering.copy()
                offering_copy["competitor"] = competitor_name
                if isinstance(offering_copy.get("available_in_tiers"), list):
                    offering_copy["available_in_tiers"] = ", ".join(offering_copy["available_in_tiers"])
                groups_offerings.append(offering_copy)

            # --- Service offerings ---
            for svc in data.get("service_offerings", []):
                svc_copy = svc.copy()
                svc_copy["competitor"] = competitor_name
                service_offerings.append(svc_copy)

            # --- Insurance offerings ---
            for ins in data.get("insurance_offerings", []):
                ins_copy = ins.copy()
                ins_copy["competitor"] = competitor_name
                if isinstance(ins_copy.get("available_in_tiers"), list):
                    ins_copy["available_in_tiers"] = ", ".join(ins_copy["available_in_tiers"])
                insurance_offerings.append(ins_copy)

            # --- Market intelligence ---
            mi = data.get("market_intelligence")
            if mi:
                mi_copy = mi.copy() if isinstance(mi, dict) else mi.__dict__
                mi_copy["competitor"] = competitor_name
                if isinstance(mi_copy.get("target_market_segments"), list):
                    mi_copy["target_market_segments"] = ", ".join(mi_copy["target_market_segments"])
                if isinstance(mi_copy.get("recent_news"), list):
                    mi_copy["recent_news"] = "; ".join(mi_copy["recent_news"])
                if isinstance(mi_copy.get("known_challenges"), list):
                    mi_copy["known_challenges"] = "; ".join(mi_copy["known_challenges"])
                market_intelligence.append(mi_copy)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # -----------------------------------------------------------------------
    # Phase 2: Comparison JSON (run_detailed_comparison outputs)
    # -----------------------------------------------------------------------
    care_aide_comparisons = []
    branded_from_comparisons = []

    comp_files = glob(os.path.join(comp_dir, "*.json")) if os.path.exists(comp_dir) else []

    for file_path in comp_files:
        competitor_name = (
            os.path.basename(file_path)
            .replace("sp_vs_", "")
            .replace(".json", "")
            .capitalize()
        )
        print(f"Processing comparison: SimplePractice vs {competitor_name}...")

        try:
            with open(file_path, "r") as f:
                data = json.load(f)

            # --- Care Aide capability gaps ---
            for gap in data.get("care_aide_capability_comparison", []):
                gap_copy = gap.copy()
                gap_copy["competitor"] = competitor_name
                care_aide_comparisons.append(gap_copy)

            # --- Branded solutions surfaced during comparison ---
            for sol in data.get("branded_solutions", []):
                sol_copy = sol.copy()
                sol_copy["competitor"] = competitor_name
                sol_copy["source"] = "comparison"
                if isinstance(sol_copy.get("core_capabilities"), list):
                    sol_copy["core_capabilities"] = "; ".join(sol_copy["core_capabilities"])
                branded_from_comparisons.append(sol_copy)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # -----------------------------------------------------------------------
    # Write CSVs
    # -----------------------------------------------------------------------

    # --- General features ---
    if all_features:
        df = pd.DataFrame(all_features)
        cols = ["competitor"] + [c for c in df.columns if c != "competitor"]
        df = df[cols]
        output_path = f"{base_dir}/compiled_features.csv"
        df.to_csv(output_path, index=False)
        print(f"\nCompiled {len(all_features)} general features → {output_path}")
    else:
        print("No general features found to compile.")

    # --- AI features ---
    if ai_features:
        df_ai = pd.DataFrame(ai_features)
        df_ai = df_ai.drop(columns=["ai_maturity_summary"], errors="ignore")
        priority_cols = [
            "competitor", "feature_name", "description", "underlying_technology",
            "automation_level", "is_gated", "available_in_tiers", "data_privacy_notes",
        ]
        cols = priority_cols + [c for c in df_ai.columns if c not in priority_cols]
        df_ai = df_ai[[c for c in cols if c in df_ai.columns]]
        output_path_ai = f"{base_dir}/compiled_ai_features.csv"
        df_ai.to_csv(output_path_ai, index=False)
        print(f"Compiled {len(ai_features)} AI features → {output_path_ai}")
    else:
        print("No AI features found to compile.")

    # --- AI maturity summary (one row per competitor) ---
    maturity_rows = []
    for file_path in json_files:
        competitor_name = os.path.basename(file_path).replace(".json", "").capitalize()
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            summary = data.get("ai_maturity_summary", "")
            ai_count = len(data.get("ai_features", []))
            if summary:
                maturity_rows.append({
                    "competitor": competitor_name,
                    "ai_feature_count": ai_count,
                    "ai_maturity_summary": summary,
                })
        except Exception as e:
            print(f"Error reading maturity summary for {file_path}: {e}")

    if maturity_rows:
        df_maturity = pd.DataFrame(maturity_rows)
        maturity_path = f"{base_dir}/ai_maturity_summary.csv"
        df_maturity.to_csv(maturity_path, index=False)
        print(f"Compiled AI maturity summaries → {maturity_path}")
    else:
        print("No AI maturity summaries found to compile.")

    # --- Branded solutions (merged from raw + comparison sources) ---
    all_branded = branded_solutions + branded_from_comparisons
    if all_branded:
        df_branded = pd.DataFrame(all_branded)
        # Deduplicate on competitor + solution_name
        if "solution_name" in df_branded.columns:
            df_branded = df_branded.drop_duplicates(subset=["competitor", "solution_name"], keep="first")
        priority_cols = [
            "competitor", "solution_name", "thematic_description", "core_capabilities",
            "target_user", "ai_powered", "pricing_model", "url_or_source", "source",
        ]
        cols = priority_cols + [c for c in df_branded.columns if c not in priority_cols]
        df_branded = df_branded[[c for c in cols if c in df_branded.columns]]
        branded_path = f"{base_dir}/branded_solutions.csv"
        df_branded.to_csv(branded_path, index=False)
        print(f"Compiled {len(df_branded)} branded solutions → {branded_path}")
    else:
        print("No branded solutions found to compile.")

    # --- Groups offerings ---
    if groups_offerings:
        df_groups = pd.DataFrame(groups_offerings)
        priority_cols = [
            "competitor", "feature_name", "description", "included_in_base_plan",
            "available_in_tiers", "groups_capacity_limits", "pricing_model",
            "customer_benefit", "comparison_to_simplepractice",
        ]
        cols = priority_cols + [c for c in df_groups.columns if c not in priority_cols]
        df_groups = df_groups[[c for c in cols if c in df_groups.columns]]
        groups_path = f"{base_dir}/groups_offerings.csv"
        df_groups.to_csv(groups_path, index=False)
        print(f"Compiled {len(groups_offerings)} groups offerings → {groups_path}")
    else:
        print("No groups offerings found to compile.")

    # --- Service offerings ---
    if service_offerings:
        df_services = pd.DataFrame(service_offerings)
        priority_cols = [
            "competitor", "category", "offering_name", "description",
            "is_dedicated_resource", "number_of_sessions", "availability",
            "pricing", "publicly_documented",
        ]
        cols = priority_cols + [c for c in df_services.columns if c not in priority_cols]
        df_services = df_services[[c for c in cols if c in df_services.columns]]
        
        # Sort by category for better organization
        if "category" in df_services.columns:
            category_order = {
                "Data Transfer/Switching": 0,
                "Onboarding": 1,
                "Customer Success": 2,
            }
            df_services["_sort"] = df_services["category"].map(category_order).fillna(99)
            df_services = df_services.sort_values(["_sort", "competitor"]).drop(columns=["_sort"])
        
        services_path = f"{base_dir}/service_offerings.csv"
        df_services.to_csv(services_path, index=False)
        print(f"Compiled {len(service_offerings)} service offerings → {services_path}")
    else:
        print("No service offerings found to compile.")

    # --- Insurance offerings ---
    if insurance_offerings:
        df_insurance = pd.DataFrame(insurance_offerings)
        priority_cols = [
            "competitor", "offering_name", "description", "supported_payers",
            "claim_submission", "era_support", "eligibility_verification",
            "available_in_tiers", "pricing_model",
        ]
        cols = priority_cols + [c for c in df_insurance.columns if c not in priority_cols]
        df_insurance = df_insurance[[c for c in cols if c in df_insurance.columns]]
        insurance_path = f"{base_dir}/insurance_offerings.csv"
        df_insurance.to_csv(insurance_path, index=False)
        print(f"Compiled {len(insurance_offerings)} insurance offerings → {insurance_path}")
    else:
        print("No insurance offerings found to compile.")

    # --- Market intelligence ---
    if market_intelligence:
        df_market = pd.DataFrame(market_intelligence)
        priority_cols = [
            "competitor", "market_scope", "target_market_segments",
            "market_positioning", "recent_news", "known_challenges",
        ]
        cols = priority_cols + [c for c in df_market.columns if c not in priority_cols]
        df_market = df_market[[c for c in cols if c in df_market.columns]]
        market_path = f"{base_dir}/market_intelligence.csv"
        df_market.to_csv(market_path, index=False)
        print(f"Compiled {len(market_intelligence)} market intelligence records → {market_path}")
    else:
        print("No market intelligence found to compile.")

    # --- Care Aide capability comparisons / gap table ---
    if care_aide_comparisons:
        df_gaps = pd.DataFrame(care_aide_comparisons)
        priority_cols = [
            "competitor",
            "capability_area",
            "care_aide_status",
            "care_aide_description",
            "competitor_branded_name",
            "competitor_status",
            "competitor_description",
            "gap_direction",
            "gap_severity",
            "gap_notes",
        ]
        cols = priority_cols + [c for c in df_gaps.columns if c not in priority_cols]
        df_gaps = df_gaps[[c for c in cols if c in df_gaps.columns]]

        # Sort by severity for easy triage: critical → moderate → minor → none
        severity_order = {"critical": 0, "moderate": 1, "minor": 2, "none": 3}
        if "gap_severity" in df_gaps.columns:
            df_gaps["_sort"] = df_gaps["gap_severity"].str.lower().map(severity_order).fillna(99)
            df_gaps = df_gaps.sort_values(["_sort", "competitor", "capability_area"]).drop(columns=["_sort"])

        gaps_path = f"{base_dir}/care_aide_capability_gaps.csv"
        df_gaps.to_csv(gaps_path, index=False)
        print(f"Compiled {len(df_gaps)} Care Aide capability gap rows → {gaps_path}")

        # Also write a pivot summary: capability area × competitor → gap direction
        try:
            pivot = df_gaps.pivot_table(
                index="capability_area",
                columns="competitor",
                values="gap_direction",
                aggfunc="first",
            )
            pivot_path = f"{base_dir}/care_aide_gap_pivot.csv"
            pivot.to_csv(pivot_path)
            print(f"Gap pivot table → {pivot_path}")
        except Exception as e:
            print(f"Could not generate gap pivot table: {e}")
    else:
        print("No Care Aide capability comparison data found (run --compare to generate this).")

    # -----------------------------------------------------------------------
    # Generate Markdown Summary Report
    # -----------------------------------------------------------------------
    generate_markdown_summary(
        base_dir=base_dir,
        date_str=output_folder_name,
        json_files=json_files,
        all_features=all_features,
        ai_features=ai_features,
        branded_solutions=all_branded,
        groups_offerings=groups_offerings,
        service_offerings=service_offerings,
        insurance_offerings=insurance_offerings,
        market_intelligence=market_intelligence,
        maturity_rows=maturity_rows,
        focus_name=focus_name
  )


    print(f"\n{'=' * 80}")
    print("COMPILATION COMPLETE")
    print(f"{'=' * 80}")
    print(f"All outputs saved to: {base_dir}")


def generate_markdown_summary(
    base_dir,
    date_str,
    json_files,
    all_features,
    ai_features,
    branded_solutions,
    groups_offerings,
    service_offerings,
    insurance_offerings,
    market_intelligence,
    maturity_rows,
    focus_name=None,
):
    """Generate a focus-aware markdown summary report."""

    import os
    import json

    summary_path = f"{base_dir}/summary_report.md"
    competitors = sorted(
        list(set([os.path.basename(f).replace(".json", "").capitalize() for f in json_files]))
    )

    def bullet_list(items, empty_text="None identified.", limit=None):
        if not items:
            return f"- {empty_text}\n"
        rows = items[:limit] if limit else items
        return "".join([f"- {item}\n" for item in rows])

    with open(summary_path, "w") as f:
        f.write(f"# Competitive Research Summary\n\n")
        if focus_name:
            f.write(f"**Focus Area:** {focus_name}\n\n")
        f.write(f"**Generated:** {date_str}\n\n")
        f.write(f"**Competitors Analyzed:** {', '.join(competitors)}\n\n")
        f.write("---\n\n")

        for file_path in json_files:
            competitor_name = os.path.basename(file_path).replace(".json", "").capitalize()

            try:
                with open(file_path, "r") as json_file:
                    data = json.load(json_file)

                f.write(f"## {competitor_name}\n\n")

                pricing_tiers = data.get("pricing_tiers", [])
                general_features = data.get("all_features", [])
                ai_feats = data.get("ai_features", [])
                branded = data.get("branded_solutions", [])
                groups = data.get("groups_offerings", [])
                services = data.get("service_offerings", [])
                insurance = data.get("insurance_offerings", [])
                tech_constraints = data.get("technical_constraints", [])
                add_costs = data.get("additional_costs", [])
                ai_summary = data.get("ai_maturity_summary", "")
                mi = data.get("market_intelligence")
                mi_data = mi if isinstance(mi, dict) else (mi.__dict__ if mi else {})

                # AI Features & Capabilities
                if focus_name == "AI Features & Capabilities":
                    f.write("### AI Product Overview\n\n")
                    f.write(f"- AI features found: {len(ai_feats)}\n")
                    f.write(f"- Branded AI solutions found: {len(branded)}\n\n")

                    f.write("### Branded AI Solutions\n\n")
                    if branded:
                        for sol in branded:
                            s = sol if isinstance(sol, dict) else sol.__dict__
                            f.write(f"- **{s.get('solution_name', 'N/A')}**: {s.get('thematic_description', '')}\n")
                    else:
                        f.write("- No branded AI solutions identified.\n")
                    f.write("\n")

                    f.write("### Core AI Features\n\n")
                    if ai_feats:
                        for feat in ai_feats:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            tech = ft.get("underlying_technology")
                            gated = " [GATED]" if ft.get("is_gated") else ""
                            if tech:
                                f.write(f"- **{ft.get('feature_name', 'N/A')}** ({tech}){gated}: {ft.get('description', '')}\n")
                            else:
                                f.write(f"- **{ft.get('feature_name', 'N/A')}**{gated}: {ft.get('description', '')}\n")
                    else:
                        f.write("- No AI features identified.\n")
                    f.write("\n")

                    f.write("### AI Privacy, Compliance, and Technical Notes\n\n")
                    f.write(bullet_list(tech_constraints, "No technical or compliance notes identified."))
                    f.write("\n")

                    f.write("### AI Pricing / Gating\n\n")
                    if pricing_tiers:
                        for tier in pricing_tiers:
                            t = tier if isinstance(tier, dict) else tier.__dict__
                            f.write(f"- **{t.get('tier_name', 'N/A')}**: {t.get('price', 'N/A')}\n")
                    if add_costs:
                        for cost in add_costs:
                            f.write(f"- {cost}\n")
                    if not pricing_tiers and not add_costs:
                        f.write("- No AI pricing or gating details identified.\n")
                    f.write("\n")

                    f.write("### Short Summary\n\n")
                    f.write(f"{ai_summary or 'No AI maturity summary available.'}\n\n")

                # Groups & Service Offerings
                elif focus_name == "Groups & Service Offerings":
                    f.write("### Group Practice Capabilities\n\n")
                    if groups:
                        for offering in groups:
                            o = offering if isinstance(offering, dict) else offering.__dict__
                            f.write(f"- **{o.get('feature_name', 'N/A')}**: {o.get('description', '')}\n")
                    else:
                        f.write("- No group-practice-specific capabilities identified.\n")
                    f.write("\n")

                    f.write("### Insurance & Billing Support for Group Practices\n\n")
                    if insurance:
                        for ins in insurance:
                            i = ins if isinstance(ins, dict) else ins.__dict__
                            f.write(f"- **{i.get('offering_name', 'N/A')}**: {i.get('description', '')}\n")
                    else:
                        f.write("- No group-relevant insurance support identified.\n")
                    f.write("\n")

                    f.write("### Service Offerings\n\n")
                    if services:
                        for svc in services:
                            sv = svc if isinstance(svc, dict) else svc.__dict__
                            f.write(f"- **[{sv.get('category', 'Other')}] {sv.get('offering_name', 'N/A')}**: {sv.get('description', '')}\n")
                    else:
                        f.write("- No service offerings identified.\n")
                    f.write("\n")

                    f.write("### Relevant AI in This Area\n\n")
                    if ai_feats:
                        for feat in ai_feats:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- **{ft.get('feature_name', 'N/A')}**: {ft.get('description', '')}\n")
                    else:
                        f.write("- No AI directly relevant to this area was identified.\n")
                    f.write("\n")

                    f.write("### Key Limitations or Missing Capabilities\n\n")
                    f.write(bullet_list(tech_constraints, "No major limitations identified."))
                    f.write("\n")

                    f.write("### Pricing / Gating Notes\n\n")
                    f.write(bullet_list(add_costs, "No additional cost or gating notes identified."))
                    f.write("\n")

                    f.write("### Short Summary\n\n")
                    if mi_data.get("market_positioning"):
                        f.write(f"{mi_data.get('market_positioning')}\n\n")
                    else:
                        f.write("No concise market summary available.\n\n")

                # Pricing & Packaging
                elif focus_name == "Pricing & Packaging":
                    f.write("### Pricing Model Overview\n\n")
                    if pricing_tiers:
                        f.write(f"- Pricing tiers found: {len(pricing_tiers)}\n")
                    else:
                        f.write("- No pricing tiers clearly identified.\n")
                    f.write("\n")

                    f.write("### Pricing Tiers and What's Included\n\n")
                    if pricing_tiers:
                        for tier in pricing_tiers:
                            t = tier if isinstance(tier, dict) else tier.__dict__
                            features = t.get("key_features", [])
                            feature_text = ", ".join(features) if features else "No included feature details captured"
                            f.write(f"- **{t.get('tier_name', 'N/A')}**: {t.get('price', 'N/A')} — {feature_text}\n")
                    else:
                        f.write("- No detailed pricing tier information identified.\n")
                    f.write("\n")

                    f.write("### Add-Ons, Gating, and Upsell Strategy\n\n")
                    f.write(bullet_list(add_costs, "No add-ons or upsell notes identified."))
                    f.write("\n")

                    f.write("### Relevant AI / Premium Packaging Notes\n\n")
                    if ai_feats:
                        for feat in ai_feats:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- **{ft.get('feature_name', 'N/A')}**: {ft.get('description', '')}\n")
                    else:
                        f.write("- No AI packaging notes identified.\n")
                    f.write("\n")

                    f.write("### Key Limitations or Complexity in Pricing\n\n")
                    f.write(bullet_list(tech_constraints, "No notable pricing complexity captured."))
                    f.write("\n")

                    f.write("### Short Summary\n\n")
                    f.write("This summary highlights the competitor's packaging model, add-ons, and pricing complexity.\n\n")

                # Documentation & Clinical Workflows
                elif focus_name == "Documentation & Clinical Workflows":
                    f.write("### Documentation Workflow Overview\n\n")
                    if general_features:
                        f.write(f"- Documentation-related features found: {len(general_features)}\n")
                    else:
                        f.write("- No documentation-specific features clearly identified.\n")
                    f.write("\n")

                    f.write("### Core Note and Treatment Plan Capabilities\n\n")
                    if general_features:
                        for feat in general_features:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- **{ft.get('feature_name', 'N/A')}**: {ft.get('description', '')}\n")
                    else:
                        f.write("- No core documentation capabilities identified.\n")
                    f.write("\n")

                    f.write("### Workflow Support Before, During, and After Sessions\n\n")
                    if tech_constraints:
                        for item in tech_constraints:
                            f.write(f"- {item}\n")
                    else:
                        f.write("- No detailed workflow-stage notes identified.\n")
                    f.write("\n")

                    f.write("### Relevant AI Features in This Area\n\n")
                    if ai_feats:
                        for feat in ai_feats:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- **{ft.get('feature_name', 'N/A')}**: {ft.get('description', '')}\n")
                    else:
                        f.write("- No AI directly relevant to documentation workflows was identified.\n")
                    f.write("\n")

                    f.write("### Key Limitations or Missing Capabilities\n\n")
                    f.write(bullet_list(tech_constraints, "No major documentation limitations identified."))
                    f.write("\n")

                    f.write("### Pricing / Gating Notes\n\n")
                    if pricing_tiers:
                        for tier in pricing_tiers:
                            t = tier if isinstance(tier, dict) else tier.__dict__
                            f.write(f"- **{t.get('tier_name', 'N/A')}**: {t.get('price', 'N/A')}\n")
                    if add_costs:
                        for cost in add_costs:
                            f.write(f"- {cost}\n")
                    if not pricing_tiers and not add_costs:
                        f.write("- No pricing or gating notes identified.\n")
                    f.write("\n")

                    f.write("### Short Summary\n\n")
                    f.write("This summary highlights how the competitor supports clinical documentation, note workflows, and related AI assistance.\n\n")

                # Messaging & Collaboration
                elif focus_name == "Messaging & Collaboration":
                    f.write("### Messaging Capabilities\n\n")
                    if general_features:
                        for feat in general_features:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- **{ft.get('feature_name', 'N/A')}**: {ft.get('description', '')}\n")
                    else:
                        f.write("- No messaging-specific capabilities clearly identified.\n")
                    f.write("\n")

                    f.write("### Internal Collaboration Capabilities\n\n")
                    if services:
                        for svc in services:
                            sv = svc if isinstance(svc, dict) else svc.__dict__
                            f.write(f"- **{sv.get('offering_name', 'N/A')}**: {sv.get('description', '')}\n")
                    else:
                        f.write("- No internal collaboration workflows clearly identified.\n")
                    f.write("\n")

                    f.write("### Relevant AI Features in This Area\n\n")
                    if ai_feats:
                        for feat in ai_feats:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- **{ft.get('feature_name', 'N/A')}**: {ft.get('description', '')}\n")
                    else:
                        f.write("- No AI directly relevant to messaging/collaboration was identified.\n")
                    f.write("\n")

                    f.write("### Key Limitations or Missing Capabilities\n\n")
                    f.write(bullet_list(tech_constraints, "No major messaging or collaboration limitations identified."))
                    f.write("\n")

                    f.write("### Pricing / Gating Notes\n\n")
                    f.write(bullet_list(add_costs, "No pricing or gating notes identified."))
                    f.write("\n")

                    f.write("### Short Summary\n\n")
                    f.write("This summary highlights client communication, internal collaboration, and any AI that directly supports communication workflows.\n\n")

                # Billing & Insurance
                elif focus_name == "Billing & Insurance":
                    f.write("### Billing & Insurance Workflow Overview\n\n")
                    if insurance:
                        f.write(f"- Insurance-related capabilities found: {len(insurance)}\n")
                    else:
                        f.write("- No billing or insurance workflow details clearly identified.\n")
                    f.write("\n")

                    f.write("### Core Insurance and Claim Capabilities\n\n")
                    if insurance:
                        for ins in insurance:
                            i = ins if isinstance(ins, dict) else ins.__dict__
                            f.write(f"- **{i.get('offering_name', 'N/A')}**: {i.get('description', '')}\n")
                    else:
                        f.write("- No core insurance or claim capabilities identified.\n")
                    f.write("\n")

                    f.write("### Payment Collection and Revenue Cycle Support\n\n")
                    if services:
                        for svc in services:
                            sv = svc if isinstance(svc, dict) else svc.__dict__
                            f.write(f"- **{sv.get('offering_name', 'N/A')}**: {sv.get('description', '')}\n")
                    else:
                        f.write("- No payment collection or revenue-cycle support clearly identified.\n")
                    f.write("\n")

                    f.write("### Relevant AI Features in This Area\n\n")
                    if ai_feats:
                        for feat in ai_feats:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- **{ft.get('feature_name', 'N/A')}**: {ft.get('description', '')}\n")
                    else:
                        f.write("- No AI directly relevant to billing/insurance was identified.\n")
                    f.write("\n")

                    f.write("### Key Limitations or Missing Capabilities\n\n")
                    f.write(bullet_list(tech_constraints, "No major billing or insurance limitations identified."))
                    f.write("\n")

                    f.write("### Pricing / Gating Notes\n\n")
                    f.write(bullet_list(add_costs, "No pricing or gating notes identified."))
                    f.write("\n")

                    f.write("### Short Summary\n\n")
                    f.write("This summary highlights billing workflows, insurance capabilities, and revenue-cycle support.\n\n")

                # Fallback generic
                else:
                    f.write("### Overview\n\n")
                    f.write(f"- Pricing tiers found: {len(pricing_tiers)}\n")
                    f.write(f"- General features found: {len(general_features)}\n")
                    f.write(f"- AI features found: {len(ai_feats)}\n")
                    f.write(f"- Branded solutions found: {len(branded)}\n\n")

                    if tech_constraints:
                        f.write("### Technical Constraints\n\n")
                        f.write(bullet_list(tech_constraints))
                        f.write("\n")

                    if add_costs:
                        f.write("### Additional Costs\n\n")
                        f.write(bullet_list(add_costs))
                        f.write("\n")

                f.write(f"_Raw data source: raw/{competitor_name.lower()}.json_\n\n")
                f.write("---\n\n")

            except Exception as e:
                f.write(f"## {competitor_name}\n\n")
                f.write(f"_Error processing data: {e}_\n\n")
                f.write("---\n\n")

    print(f"Generated focus-aware markdown summary → {summary_path}")

if __name__ == "__main__":
    compile_json_to_csv()
