# data

## Skills
Select only the most relevant skills by description. If a skill matches, read its `SKILL.md` and use it before acting.

### analyze
Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigating what's driving a trend or drop, comparing segments over time, or preparing a formal data report for stakeholders.

File: `external/anthropic-knowledge-work-plugins/data/skills/analyze/SKILL.md`

### build-dashboard
Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snapshot, or needing multiple charts with filters in one browser-openable file.

File: `external/anthropic-knowledge-work-plugins/data/skills/build-dashboard/SKILL.md`

### create-viz
Create publication-quality visualizations with Python. Use when turning query results or a DataFrame into a chart, selecting the right chart type for a trend or comparison, generating a plot for a report or presentation, or needing an interactive chart with hover and zoom.

File: `external/anthropic-knowledge-work-plugins/data/skills/create-viz/SKILL.md`

### data-visualization
Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creating publication-quality figures, or applying design principles like accessibility and color theory.

File: `external/anthropic-knowledge-work-plugins/data/skills/data-visualization/SKILL.md`

### dbt
Skills for analytics engineering with dbt - building models, writing tests, querying the semantic layer, troubleshooting jobs, and more. Use when doing any dbt analytics engineering work.

File: `external/kilo-marketplace-skills/skills/dbt/SKILL.md`

### dbt-migration
Skills for migrating dbt projects - moving from dbt Core to the Fusion engine or across data platforms. Use when migrating dbt projects between platforms or to dbt Fusion.

File: `external/kilo-marketplace-skills/skills/dbt-migration/SKILL.md`

### explore-data
Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and column distributions, spotting data quality issues like duplicates or suspicious values, or deciding which dimensions and metrics to analyze.

File: `external/anthropic-knowledge-work-plugins/data/skills/explore-data/SKILL.md`

### instrument-data-to-allotrope
Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

File: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`

### jupyter-notebook
Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

File: `external/openai-skills/skills/.curated/jupyter-notebook/SKILL.md`

### openai-jupyter-notebook
Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments,

File: `external/trailofbits-skills-curated/plugins/openai-jupyter-notebook/skills/openai-jupyter-notebook/SKILL.md`

### openai-spreadsheet
Use when tasks involve creating, editing, analyzing, or formatting spreadsheets (`.xlsx`,

File: `external/trailofbits-skills-curated/plugins/openai-spreadsheet/skills/openai-spreadsheet/SKILL.md`

### sql-queries
Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, optimizing slow SQL, translating between dialects, or building complex analytical queries with CTEs, window functions, or aggregations.

File: `external/anthropic-knowledge-work-plugins/data/skills/sql-queries/SKILL.md`

### statistical-analysis
Apply statistical methods including descriptive stats, trend analysis, outlier detection, and hypothesis testing. Use when analyzing distributions, testing for significance, detecting anomalies, computing correlations, or interpreting statistical results.

File: `external/anthropic-knowledge-work-plugins/data/skills/statistical-analysis/SKILL.md`

### validate-data
QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checking calculations and aggregation logic, verifying a SQL query's results look right, or assessing whether conclusions are actually supported by the data.

File: `external/anthropic-knowledge-work-plugins/data/skills/validate-data/SKILL.md`

### vercel-react-best-practices
React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.

File: `external/vercel-agent-skills/skills/react-best-practices/SKILL.md`

### write-query
Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need into SQL, building a multi-CTE query with joins and aggregations, optimizing a query against a large partitioned table, or getting dialect-specific syntax for Snowflake, BigQuery, Postgres, etc.

File: `external/anthropic-knowledge-work-plugins/data/skills/write-query/SKILL.md`

### xlsx
Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like "the xlsx in my downloads") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

File: `external/anthropic-skills/skills/xlsx/SKILL.md`
