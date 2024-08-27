# IAV Streamlit Project

This repository contains a streamlit app that showcases my professional CV and a service for joke generation with Gemini LLM.

# Structure
```
iav-app
├── services  # dir with services
│   ├── joker  # Joke generation service
│   │   ├── utils
│   │   │   ├── data_classes.py  # request classes
│   │   │   └── model.py  # gemini model class
│   │   ├── Dockerfile
│   │   ├── model_config.yaml  # default gemini config
│   │   ├── requirements.txt  # list of dependencies for the joker
│   │   └── joker.py  # LLM joker app entrypoint      
│   └── streamlit_app  # streamlit service
│       ├── pages
│       │   ├── Curriculum_Vitae.py  # CV page
│       │   └── Joker.py  # joke generation page
│       ├── utils
│       │   └── prompting.py  # prompting utilities for joke │generation     
│       └── static  # static objects for CV
│       │    ├── lgrigorian_job_cv.md  # CV in markdown format
│       │    └── lgrigorian_job_cv.pdf  # CV in pdf format
│       ├── Dockerfile
│       ├── requirements.txt  # dependencies for streamlit app               
│       └── Main_Page.py  # entrypoint for streamlit UI
├── .env  # ADD THIS! Must contain GEMINI_API_KEY
├── README.md  # repo description               
├── docker-compose.yaml
├── requirements_dev.txt  # dependencies for development (all the dependencies)
└── .gitignore              
```

# How to


1. Add an ```.env``` file with your **Google AI Studio API Key** to the root of the repository.

    ```GEMINI_API_KEY=your_api_key```

2. Run the services with\
```docker-compose -f docker-compose.yaml up --build -d```


# References

Some references that I found interesting

* [The Last Laugh: Exploring the Role of Humor as a Benchmark for Large Language Models](https://www.finn-group.com/post/the-last-laugh-exploring-the-role-of-humor-as-a-benchmark-for-large-language-models)
* [Talk Funny! A Large-Scale Humor Response Dataset with Chain-of-Humor
Interpretation](https://ojs.aaai.org/index.php/AAAI/article/view/29736/31266)
* [Prompts for writing jokes based on context](https://www.reddit.com/r/PromptEngineering/comments/178tryd/prompts_for_writing_jokes_based_on_context/)
* [Witscript 3: A Hybrid AI System for Improvising Jokes in a Conversation](https://arxiv.org/pdf/2301.02695)