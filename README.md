# MLops Final Project

## Idea

From a movie dataset and a user description, we return Movies !

**Possible datasets:**

- [1k movies](https://www.kaggle.com/datasets/akashkotal/imbd-top-1000-with-description)
- [10k movies](https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset)

So the idea is to use RAG to get k-most relevant movies descriptions and then we return them and order them by rating.

Moreover we can filter them by some other feature.

We can also have a way in the interface to change the number k of movies.

For software specification and brainstorming: [miro board](https://miro.com/welcomeonboard/c0ppclVqUGM2aysyT0t0S1liTVZoYzdVeGVTV3RtOFBIZk1wK0dCajdPUm5YSDIwaGdha3BZWTEzN0k2SWdMV0s0L1NYREt5Q2oxT1FqMGpCZDJSYnl5bWVRNitWOGhya1ZCTGdOQTBwWlBYaFVwWXNtK2VVMFdZWlJQWlBuNDYhZQ==?share_link_id=912840001517)

## Talk about issues or extensions

Already seen movies etc ...

#### To tackle this semi limitation

We want to show other films that do not include those ones. So we can get the k+1 system

### Development

- **Features**: Clearly define with diagrams, functional and non-functional requirements.
- **Tasks**: Assign roles.
- **Agile Strategy**
- **Version Control**
  - GitHub versioning control
- **Testing**
  - Macro tests, Streamlit, etc.
- **Development Cycles**
  - 1-2 times per week
  - Performance improvement graphs
  - Start with a simple workflow, then gradually advance
- **Development Priorities**
  - First, build interfaces, define request and response structures.
  - No LLM initially, find the most cost-effective first version.
  - Improve and develop as a team.
  - Final deployment perhaps using Docker

### Report

- Document the strategy with appropriate diagrams for each cycle.
- Optionally record 5-minute updates.
- Well-documented commits.

> **Note**: CI/CD is not needed for now; keep it for discussion.

### Proof of Concept

- Use some unit tests to verify that components function correctly.
