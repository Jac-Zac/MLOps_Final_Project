## 1. Introduction

### 1.1 Purpose
The purpose of this software is to recommend films to users. Based on a minimum rating value they provide, the system will return a random film with an equal or higher rating.

### 1.2 Scope
This system is designed for movie enthusiasts seeking film recommendations without a predefined selection in mind. The software will:
- Accept a minimum rating value.
- Return a random film from an IMDb-based database.

The system will be implemented as a web-based application with a backend for processing. Future extensions may include film suggestion based on description keywords.

### 1.3 Definitions, Acronyms, and Abbreviations
- **IMDb**: Internet Movie Database, a comprehensive dataset of films and related metadata.
- **TMDB**: The Movie Database, a community built movie and TV database.
- **API**: Application Programming Interface, a type of software interface, offering a service to other pieces of software. 

## 2. Overall Description
### 2.1 Product Perspective
This software is a standalone, data-driven web application designed to assist users in selecting a film to watch. It leverages advanced data processing techniques to generate recommendations based on user-provided input. The system features an intuitive and interactive user interface, that facilitates seamless data entry and presents the output in a structured and accessible manner.

### 2.2 Product Functions
**Randomized suggestion** user will be able to specify a minimum rating value via a slider, and the system will retrieve and present a randomly selected film that meets this creteria.

### 2.3 User Characteristics
- **Casual Users** Users who wish to explore cinema, but have limited expertise in film culture.
- **Film Enthusiasts** Users seeking to discover new content, without being influenced by descriptions or criteria-based selections.

### 2.4 Constraints
- Individuals lacking internet access will be unable to utilize the software.
- The system language will be English.

### 2.5 Assumptions and Dependencies
- The dataset used for recommendations will be regularly updated.
- The system will require a stable internet connection for database queries.

## 3. Specific Requirements
The system should allow users to easily explore films by providing a simple and intuitive interface. Users will be able to select a minimum movie rating through a slider, ranging from 0 to 10, which will filter the films based on their preference. Once the desired rating is set, users can press a button labeled "Pick Random Film," prompting the system to return a random film recommendation that meets the rating criteria. Along with the film title, the system will provide key details such as the release year, duration, rating, number of votes, and a brief description. Additionally, a movie poster, sourced from the TMDB database, will be displayed to complement the information.
The user interface is designed with simplicity and accessibility in mind, ensuring that users can interact with the system effortlessly and without any technical expertise. The software functions reliably, providing movie suggestions quickly. Furthermore, the system is compatible with common web browsers, making it accessible to a wide range of users.

### 3.1 Functional Requirements
**User Input Handling** The system shall provide a slider interface for users to select a minimum rating value, ranging from 0 to 10. The selected value will be used as a filter criterion for selecting films.  
The system shall include a "Pick Random Film" button that, when pressed, triggers the system to filter the IMDb database and return a randomly selected film that meets the rating requirement.  
**Movie Retrieval and Filtering** The system shall query the IMDb database to retrieve films with a rating equal to or higher than the user-selected rating value. The filtered films will then be randomly selected.  
For each selected film, the system shall retrieve the following data:
 - Title
 - Year
 - Duration
 - Rating
 - Votes
 - Description

**Movie Poster Retrieval** The system shall use the TMDB API to fetch the movie poster corresponding to the randomly selected film. The poster shall be displayed alongside the other movie details.

### 3.2 Performance Requirements
**Response Time** The system shall return the randomly selected film, along with its details, within 3 seconds of the user pressing the "Pick Random Film" button, assuming a stable internet connection.  
The system shall ensure that the time required to filter the IMDb database and retrieve the movie poster from the TMDB API does not exceed 2 seconds.  
**Concurrency** The system should be able to handle at least 100 concurrent users requesting random films without significant degradation in performance or responsiveness.  
**Accuracy of Data** The system shall ensure that only films with ratings greater than or equal to the user-selected value are returned in the filtered result.

### 3.3 Interface Requirements
**User Interface** The system shall provide an intuitive, web-based user interface with the following elements:
 - A slider to select the minimum rating value.
 - A "Pick Random Film" button to trigger the film selection process.
 - A display area to show the movie title, year, duration, rating, votes, description, and poster.

**API Integration** The system shall integrate with the IMDb database to filter and retrieve films based on user input.  
The system shall also integrate with the TMDB API to retrieve and display the movie poster for the selected film.  
**Error Handling** The system shall provide clear, user-friendly error messages in case of:
 - Failed communication with IMDb or TMDB APIs.
 - No films meeting the specified rating criteria.
 - Issues with retrieving or displaying the movie poster.

### 3.4 Operational Requirements
**System Availability** The system should be operational 24/7, with an uptime of at least 99.5%.  
In the event of a service interruption (e.g., failure to connect to IMDb or TMDB), the system shall display a message informing the user of the issue.  
**System Updates and Maintenance** The system shall allow for periodic updates to the list of films in the IMDb database.  
The system should be designed to accommodate future integration with other movie databases or services.
**Scalability** The system shall be designed to scale efficiently to accommodate an increase in the number of users and queries. This could include horizontal scaling, load balancing, and optimized database queries.

### 3.5 Safety and Security Requirements
**Data Security** The system shall ensure that all communication with external APIs (IMDb and TMDB) is encrypted using secure protocols such as HTTPS.  
The system shall not store any personal data from users, as the only input is the movie rating filter.  
**API Key Protection** API keys for accessing IMDb and TMDB services must be securely stored and not exposed in client-side code or logs. The system shall use environment variables or secure vaults for managing keys.  
**Access Control** The system shall not require user authentication for accessing film recommendations but shall ensure that any interactions with external APIs are properly authorized and comply with service terms.

### 3.6 Software Quality Attributes
**Usability** The system shall have an intuitive interface for ease of use.  
**Scalability** The system shall support increasing dataset size without major performance drops.  
**Maintainability** The system shall be modular to allow easy updates and improvements.  

## 4. Supporting Information
The reference dataset is [IMDb-based](https://www.kaggle.com/datasets/akashkotal/imbd-top-1000-with-description).

## 5. Appendices
TMDB API [documentation](https://developer.themoviedb.org/docs/getting-started).

## 6. Index
- [1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Scope](#12-scope)
  - [1.3 Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
- [2. Overall Description](#2-overall-description)
  - [2.1 Product Perspective](#21-product-perspective)
  - [2.2 Product Functions](#22-product-functions)
  - [2.3 User Characteristics](#23-user-characteristics)
  - [2.4 Constraints](#24-constraints)
  - [2.5 Assumptions and Dependencies](#25-assumptions-and-dependencies)
- [3. Specific Requirements](#3-specific-requirements)
  - [3.1 Functional Requirements](#31-functional-requirements)
  - [3.2 Performance Requirements](#32-performance-requirements)
  - [3.3 Interface Requirements](#33-interface-requirements)
  - [3.4 Operational Requirements](#34-operational-requirements)
  - [3.5 Safety and Security Requirements](#35-safety-and-security-requirements)
  - [3.6 Software Quality Attributes](#36-software-quality-attributes)
- [4. Supporting Information](#4-supporting-information)
- [5. Appendices](#5-appendices)
- [6. Index](#6-index)
