# AutoVC: Zero-Shot Voice Style Transfer with Only Autoencoder Loss
CS753 Hacker Role
---

## Presentation
 - [Link](https://docs.google.com/presentation/d/1SSWw2owzS-GC6EGGR4HzgFqUVDDyQTRdJQv6bB0Xvq0/edit?usp=sharing)

## AutoVC_train.ipynb
This python notebook contains the code for training the AutoVC model from scratch. Since complete training takes quite some time, only 4 speakers from VCTK corpus with 10 audios frorm each speaker was used for training. It took around an hour to run. Number of iterations, early stopping and other hyperparameters were changed to suit the training. Encoder, decoder, generator class module were coded by referring to paper. Some help was taken for writing forward pass for them from official implementation.
Online implementation did not support checkpointing at fixed intervals. We add this functionality as well as an option of saving the model at end.

## Testcases.ipynb
This python notebook contains inference results. Pretrained modules were used for autovc, speaker encoder, vocoder (hifi gan). It was found that one test sample gave proper style transfer results qualitatively. For other audio files which were tried, output was squeaky, with words not clearly discrenible. Two types of speaker encoder viz gru_embedder and convgru_embedder were tried. They require inputs in different formats, bitrate. An attempt was made to figure out why zero shot style transfer failed for our given test audio by examining input, architecture specifications of pretrained modules. 

## Speaker_Verification.ipynb
To verify the effectivness of speaker encoder, the obtained embeddings were used for speaker verification task by taking their dot product with the same 4 speakers chosen for training. Heatmap of minimum and maximum alignment scores was found. Finally it was testesd with audio files of the group members and threshold was set by referring to heatmap. It was seen that for all audio pairs it could correctly identify whether the speakers of two files were same or not.

## Drive Folder 
- [Link](https://drive.google.com/drive/folders/1qWQwfDq56-I38shvF8oK-RW9bskBGg3h?usp=sharing)
- It contains the poster as well as wav files for the Speaker_Verification.ipynb.

## References
- [Paper](http://proceedings.mlr.press/v97/qian19c/qian19c.pdf)
- [Supplementary](http://proceedings.mlr.press/v97/qian19c/qian19c-supp.pdf)
- [Official Code](https://github.com/auspicious3000/autovc)
- [Unofficial Implementation](https://github.com/RF5/simple-autovc)
- [Official Demo](https://auspicious3000.github.io/autovc-demo/)
