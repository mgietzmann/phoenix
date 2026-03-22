# Haven Visualizer

## Overview

[paragraph] Haven Visualizer is a locally-run, AI-powered web app that lets non-technical fish biologists query and visualize spatial, environmental, and telemetry data from the Gulf of Alaska through a conversational chat interface.
> Supporting
> - Target users understand the science (telemetry, fish behavior, oceanography) but do not know SQL and have worked primarily with Excel/CSV and maybe R
> - Data includes spatial/environmental layers (temperature, H3 cells), fish telemetry (positions, depths, time series), and other Gulf of Alaska datasets
> - The app removes the technical barrier between a scientist and the database — they just ask questions
> - Name: Haven Visualizer


## Architecture

[diagram] System overview: user browser → local web app (chat UI) → AI agent → database + data sources
> Notes
> - Container is the deployment unit — user runs docker pull then docker run
> - Web app opens on localhost; not hosted publicly
> - AI agent sits between the chat UI and the database, using MCP server context to know which tables/sources to query for which kinds of questions
> - Credentials (AI API key + database) are stored persistently so a container restart within the valid credential window doesn't require re-entry

[paragraph] The app is packaged as a Docker image so that any team member can run it locally with a single docker pull, without needing to install dependencies or configure environments.
> Supporting
> - Local-only deployment is intentional: avoids security complexity of hosting, avoids paying for arbitrary external usage, and keeps data within the group's control
> - Proof-of-concept phase — want to validate the idea works well before thinking about hosting
> - Users get updates by pulling a new image

[paragraph] The AI agent is given context about the available data sources through an MCP server, so it knows where to look for each kind of data without the user having to specify table names or data locations.
> Supporting
> - MCP servers provide structured context: what data exists, what tables/columns are available, what spatial and temporal coverage each source has
> - Marcel needs to do more learning on MCP server design before specifying this fully
> - This context is baked into the image at build time (not dynamically registered by end users — see Questions)


## User Flow

[enumeration] The user flow from first launch to visualization has three phases:
> Supporting
> - **Credential setup:** on first run, the chat prompts the user to enter (1) their AI API key so usage is billed to the project account, not Marcel's, and (2) database credentials. These are saved persistently so a container restart doesn't require re-entry as long as the creds are still valid.
> - **Question and answer:** once credentials are set, the user simply chats — ask a question, get an answer, request a figure, explore data conversationally
> - **Figure download:** any figure generated in the chat can be downloaded as a static image, bundled with the code that produced it


## Visualization and Download

[paragraph] Every figure produced in the app must be downloadable as a static image alongside the code that generated it, so scientists can use the output in papers and reproduce or modify the analysis later.
> Supporting
> - Download includes: (1) the static figure at current view/selection, and (2) the code that was used to generate it
> - Code provenance is important — if the figure ends up in a paper, the analyst needs to be able to show how it was made
> - Example request: "show all Chinook tracks in Southeast Alaska in June, July, August as positions on a globe, overlaid with average temperature per H3 cell for those months"


## Deployment and Data Source Management

[paragraph] New data sources are added by updating the image rather than through an in-app registration flow, keeping the deployment model simple while Marcel is the sole data producer.
> Supporting
> - Marcel is currently the only one adding data, so committing a new image when a new source is added is acceptable overhead
> - Context for the AI agent (table descriptions, spatial/temporal coverage, etc.) lives in the repository and gets baked into the image at build time
> - End users just docker pull to get an updated app with new data sources
> - The in-app data source registration idea was considered and set aside — too much complexity for now
