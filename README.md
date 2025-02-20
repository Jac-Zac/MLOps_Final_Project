# PickaFilm

[![Tests](https://github.com/jac-zac/PickaFilm/actions/workflows/ci.yml/badge.svg)](https://github.com/jac-zac/PickaFilm/actions/workflows/ci.yml)
[![Docs](https://github.com/jac-zac/PickaFilm/actions/workflows/deploy_docs.yml/badge.svg)](https://github.com/jac-zac/PickaFilm/actions/workflows/deploy_docs.yml)

> Click the button below to access the APP

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pickafilm.streamlit.app/)

## Idea

From a movie dataset and a user description, we return Movies!

## Documentation

For detailed information, please see our [Documentation](https://jac-zac.github.io/PickaFilm/).

### Possible Datasets

- [1k movies](https://www.kaggle.com/datasets/akashkotal/imbd-top-1000-with-description)
- [10k movies](https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset)
- [TMDB n movies](https://developer.themoviedb.org/docs/getting-started)

The idea is to use Retrieval-Augmented Generation (RAG) to get the **k-most relevant movie descriptions**, order them by rating, and filter them by other features.
It is also possible to select just a minimum rating or genre.
We also provide an interface to adjust the number of **k** movies retrieved.

For software specifications and brainstorming, see our [Miro board](https://miro.com/welcomeonboard/c0ppclVqUGM2aysyT0t0S1liTVZoYzdVeGVTV3RtOFBIZk1wK0dCajdPUm5YSDIwaGdha3BZWTEzN0k2SWdMV0s0L1NYREt5Q2oxT1FqMGpCZDJSYnl5bWVRNitWOGhya1ZCTGdOQTBwWlBYaFVwWXNtK2VVMFdZWlJQWlBuNDYhZQ==?share_link_id=912840001517).

## Talk About Issues or Extensions

### Already Seen Movies

To tackle this **limitation**, we introduce a **k+1 system** to avoid recommending already seen movies and suggest fresh alternatives.

## Development Workflow

### Development Strategy

- **Features**: Clearly define with diagrams, functional and non-functional requirements.
- **Tasks**: Assign roles.
- **Agile Strategy**
- **Pair programming**
- **Version Control**: GitHub for versioning.
- **Testing**: Unit tests with `pytest`, UI tests for Streamlit.
- **Development Cycles**:
  - 1-2 updates per week.
  - Performance improvement tracking.
  - Start with a simple workflow, then enhance incrementally.
- **Priorities**:
  - **Phase 1**: Build interfaces, define request/response structures.
  - **Phase 2**: No LLM initially—find a cost-effective first version.
  - **Phase 3**: Optimize and iterate as a team.
  - **Final Deployment**: Possibly using Docker.

### Reporting and Documentation

- **Strategy Documentation**: Include diagrams for each cycle.
- **Optional Updates**: 5-minute progress recordings.
- **Well-Documented Commits**: Clear, structured messages.

> **Note:** CI/CD is not needed for now; keep it open for discussion.

## Proof of Concept

- Implement unit tests to validate the core components.
- Ensure smooth integration with Streamlit.
