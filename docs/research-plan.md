# Research plan

**Main question:** Which Edmonton neighbourhoods consistently have the most pothole reports?

**Status:** Draft for Estella and Kaleb to review. Prepared with AI assistance. No neighbourhood findings have been produced.

## 1. Plan and prepare

We want to identify neighbourhoods that repeatedly have high reporting counts. This is a descriptive study of existing 311 records.

Use [Edmonton's official 311 dataset](https://data.edmonton.ca/d/q7ua-agfg). We propose **2023–2025**: initial checks found records in all 36 months, but this does not prove the records are complete. Kaleb will confirm the usable years and neighbourhood identifiers before we start the main analysis.

Read the short [source list](sources.md) and agree on the method below. This planning step follows SCI 201.

## 2. Collect and clean the data

Keep these fields: request ID, creation date, pothole request type, and neighbourhood ID/name.

- Include road and alley pothole reports. The category also contains information inquiries, so the category alone is not a sufficient filter.
- Exclude inquiries about asphalt or repair timelines. Keep uncertain request types separate until reviewed.
- Remove repeated copies of the same request ID. Different reports may still describe the same physical pothole.
- Keep track of records with missing neighbourhoods. Do not assign them to a guessed location.
- Check neighbourhood identifiers across years. Do not combine renamed or changed areas without a verified match.
- Treat missing coverage as unknown, rather than assuming zero reports.

## 3. Analyze and interpret

1. Count eligible reports by neighbourhood and calendar year.
2. Rank neighbourhoods within each year.
3. Show the **top 10** for each year. Include ties at the cutoff and explain if the list contains more than 10.
4. Show how many years each neighbourhood appears in those lists. This is how we will describe consistency.
5. Make a neighbourhood map only after confirming compatible boundaries.

Use the same comparable neighbourhoods and complete periods for the main comparison. If the records are too incomplete, adjust the study period or simplify the comparison before drawing conclusions.

The first project focuses on counts, rankings, and clear explanations. Statistical modelling and forecasting are not part of this plan.

## 4. Write and present

The final output should include:

- A short report: question, data, method, results, limitations, and references.
- A table of yearly leaders and repeated appearances, plus a map where feasible.
- A short presentation and research poster.

## Essential limitations and data use

High reporting does not automatically mean worse roads. Counts also depend on reporting behaviour, road extent, missing information, and repeat reports.

Use neighbourhood summaries. Avoid publishing personal details or unnecessary request-level records. Check each dataset's reuse terms and required attribution before sharing data. The City licence and institutional ethics guidance are linked in [sources.md](sources.md); no ethics approval or exemption is claimed here.

## Next steps

| Person | Next action |
| --- | --- |
| **Kaleb** | Confirm the usable years, report-type filter, and neighbourhood matching; plan the count table and map. |
| **Estella** | Review the sources, check this plan and its limitations, and prepare the proposal presentation. |
| **Together** | Review the plan in PR #8, agree on the remaining data decisions, and choose a realistic schedule. |

Do not mark the proposal approved until both people have reviewed it. Follow the four SCI 201 phases above, then hold a short club retrospective after the project.
