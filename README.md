# Data Science Intern At Info Origin Inc.
May 2024 - August 2024

Repository for my projects as Data Science Intern at Info Origin Inc.

# Projects

1. **BBC News Articles Classification - RoBERTa with Enriched Vocabulary Layer**
   - Developed a custom RoBERTa model architecture with **added encoded vocabulary layer**.
   - Conducted EDA. Explored **Class Distribution** and **Text Length Distribution**.
   - Observed most frequent words in articles by class before and after **stop word removal**.
   - Preprocessed articles with **stemming** and **lemmatization**.
   - Tokenized articles using **RoBERTa tokenzier**.
   - Accuracy - **98%**
   - [Notebook](https://github.com/KunalSachdev2005/Data_Science_Intern_at_Info_Origin/)

2. **BBC News Articles Classification using Google's NNLM & Custom Neural Network**
   - Developed a custom neural network architecture from scratch for BBC News Articles Classification.
   - Used **Google's NNLM** model for text embeddings.
   - Defined trainig and testing **PyTorch Datasets and DataLoaders**
   - Observed model behavior across various batch sizes, epochs, and learning rates
   - Optimized model hyperparameters with **bayesian optimizaiton**.
   - Highest Accuracy - **96.4%**
   - [Notebook](https://github.com/KunalSachdev2005/Data_Science_Intern_at_Info_Origin/blob/main/BBC_News_Articles_Classification_Goolge_NNLM_%26_Bayesian_Opt.ipynb)

3. **Fine-tuning LLMs for Sentiment Analysis on SST-5**
   - Fine-tuned various language models like **DeBERTa, RoBERTa, ERNIE, DistilBERT, BERT, and GPT-2** for sentiment analysis on the SST-5 dataset.
   - Loaded the SST-5 dataset using the **datasets library**.
   - Tokenized all the examples in the dataset using corresponding tokenizer for the model.
   - Implemented **Bayesian Optimization** with **scikit-optimize**.
   - Due to computational resource limitations, I could only fully run optimization for DistilBERT and ERNIE.
   - Achieved the highest accuracy of **52.71%** with the optimized ERNIE model (highest-to-date: 59.8%)
   - [Notebook](https://github.com/KunalSachdev2005/Data_Science_Intern_at_Info_Origin/blob/main/SST5_ERNIE.ipynb)

