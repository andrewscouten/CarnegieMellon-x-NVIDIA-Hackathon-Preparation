# Cancer Subtyping

## Literature Review

### Example

[1]
[He, K., Zhang, X., Ren, S., & Sun, J. (2016). *Deep residual learning for image recognition.* In *Proceedings of the IEEE conference on computer vision and pattern recognition (CVPR)* (pp. 770–778).](https://doi.org/10.1109/CVPR.2016.90)

  - **Summary:** ResNet (Residual Network) is a deep convolutional neural network architecture designed to overcome the degradation problem that occurs when neural networks become very deep. In traditional CNNs, as more layers are added, training accuracy often saturates and then degrades due to vanishing/exploding gradients. ResNet solved this by introducing residual learning, which allows layers to learn modifications (residuals) to the input rather than entire transformations.

## Cancer Subtyping 

Looking for recent (2025) papers with cancer subtyping, open source, deep learning, federated learning...

### [1] [A Review of Advanced Deep Learning Methods of Multi-Target Segmentation for Breast Cancer WSIs](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10979932)

- **Topics:** Survey, Cancer (Breast), Segmentation, Multi-Target
- **Summary:** Offers a survey of segmentation methods and datasets for breast cancer, breaking down each dataset and its use. A great resource for similar tasks to help us pick and decipher various known datasets.

### [2] [Subtype-GAN: a deep learning approach for integrative cancer subtyping of multi-omics data](https://academic.oup.com/bioinformatics/article/37/16/2231/6143031)
- **Summary**: They used **deep representation learning (a MIMO GAN)** to fuse multi-omics (CNV, mRNA, miRNA, DNA methylation, and other omics data), then did **undepervised subtype discovery** via **consensus clustering over a Gaussian Mixture Model (GMM)**, identifying clincally meaningful cancer subtypes across 10 TCGA cohorts (BRCA, BLCA, KIRC, GBM, LUAD, PAAD, SKCM, STAD, UCEC and UVM, samples ~ 4154).
- - **Quick Knowledge Check**
  - **AE** stands for autoencoder which is a type of artificial neural network used to learn efficient codings of unlabeled data. It's a deterministic encoder -> decorder. Compact latent space
  - **VAE** stands for Variational autoencoder and is a probabilistic AE. Smooth latent space
  - **GAN** is generative adversarial network. Given a training set, this technique learns to generate new data with the same statistics as the training set. 
- **My thoughts**
- - I am not familiar with unsupervised models so I cannot give critiques to the model itself and the choices made when developing the model.
  - With that said I do wonder, as the model was trained only on TCGA data, how well it will do on different cohorts and datasets.
  - I do think this is a good example of how to use machine learning skills outside of the prior hackathon's theme. 
  - I also had a thought that although we may not use Subtype-GAN maybe we can steal the ideas and apply it to Andrew's knowledge graph.
  - - Add an unsupervised layer (AGAIN DO NOT KNOW ANYTHING ABOUT UNSUPERVISED LEARNING BUT WILLING TO LEARN)... Again do not know if necessary. 

### [3] [DeePathNet: A Transformer-Based Deep Learning Model Integrating Multiomic Data with Cancer Pathways](https://aacrjournals.org/cancerrescommun/article/4/12/3151/750577/DeePathNet-A-Transformer-Based-Deep-Learning-Model)
- **Topics**
- **Summary**
  - Datasets used: ProCan-DepMapSanger, Cancer Cell Line Encyclopedia, TCGA
  - DeePathNet is a transformer-based model that integrates multi-imic data such as genomic mutation, copy number variation (CNV), gene expression, /dNA methylation, protein intensity, and CRISPR-Cas9 data, among others, with cancer-specific biological pathways. The goal is to boost performance in drug response prediction, cancer type/ subtype classification, and pathway level biomarker discovery.
  - Github:  https://github.com/CMRI-ProCan/DeePathNet
- **My thoughts**
  - They utilize some datasets I have never heard of. Even if this is not a good example, it is filled with some great resources
  - So all of my thoughts typically go to knowlege graphs now. I was thinking this transformer model is utilized over 2D data... But what if we put this model over a knowledge graph. Could we make that happen?

### [4] [Biological Knowledge Graph-Enhanced Cancer State Prediction Network with Adjustable Connections](https://academic.oup.com/bioinformatics/article/39/9/btad570/7273783)
- Sooo I am sorta excited about this one
  
### [5] [Breast Cancer Classification with Various Optimized Deep Learning Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC12293705/#sec1-diagnostics-15-01751)

### [6] [Federated Deep Learning Enables Cancer Subtyping by Proteomics](https://pubmed.ncbi.nlm.nih.gov/40488620/)


### [7] [Advancing breast, lung and prostate cancer research with federated learning. A systematic review](https://www.nature.com/articles/s41746-025-01591-5)

- **Topics:** Survey, Cancer (Breast, Lung, Prostate), Federated Learning (FL)
- **Summary:** Breaks down common task workflows (classification, segmentation, detection, regression) from a survey of 25 papers from 2020 to 2023, with a heavy focus on FL usage (e.g. data privacy, domain adaptation, model improvement / generalisability). Has Sankey diagrams that shows typical workflows for specific inputs (really cool!).

### [8] [Collaborative assessment of the risk of postoperative progression in early-stage non-small cell lung cancer: a robust federated learning model](https://cancerimagingjournal.biomedcentral.com/articles/10.1186/s40644-025-00911-y)

- **Topics:** Cancer (Lung), Federated Learning (FL)
- **Summary:** Proposes a FL Bayesian classifier to detect post-operative progression of early-stage Non-Small Cell Lung Cancer (NSCLC). FL was used for feature extraction of CT images, where the classifier then took those features as inputs to predict LCP (lung cancer progression) or LCNP (lung cancer, no progression). Verbose in their methods about their FL strategy and data.
- **Notes:** 
> Among existing FL approaches, personalized FL [11] is particularly suitable for medical scenarios, allowing each center to choose between the aggregated global model and local models based on their needs

### [9] [A Personalized Multimodal Federated Learning Framework for Skin Cancer Diagnosis](https://www.mdpi.com/2079-9292/14/14/2880)

- **Topics:** Survey, Cancer (Skin), Federated Learning (FL)
- **Summary:** FL strategy and model that is both multi-task and accounts for missing modalities during prediction. Detailed about FL strategy and related works (including datasets, task, and input types of those works)

## Datasets for Colorectal, Breast, and Lung Cancer 






