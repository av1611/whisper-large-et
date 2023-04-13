---
license: cc-by-4.0
tags:
- audio
- automatic-speech-recognition
- hf-asr-leaderboard
language: et
model-index:
- name: TalTechNLP/whisper-large-et
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11
      type: mozilla-foundation/common_voice_11_0
      config: et
      split: test
    metrics:
    - name: Test WER
      type: wer
      value: 11.99
    - name: Test CER
      type: cer
      value: 3.21
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      config: et
      split: test
    metrics:
    - name: Test WER
      type: wer
      value: 11.22
    - name: Test CER
      type: cer
      value: 2.813
---


# Whisper-large-et

This is a Whisper-large-v2 model [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) finetuned on around 800 hours of diverse Estonian data.

## Model description
This is a general-purpose Estonian ASR model trained in the Lab of Language Technology at TalTech.


## Intended uses & limitations

This model is intended for general-purpose speech recognition, such as broadcast conversations, interviews, talks, etc.

## How to use

Use as any other Whisper model via HF transformers, or use a faster decoder like [faster-whisper](https://github.com/guillaumekln/faster-whisper).


#### Limitations and bias

Since this model was trained on mostly broadcast speech and texts from the web, it might have problems correctly decoding the following:
  * Speech containing technical and other domain-specific terms
  * Children's speech
  * Non-native speech
  * Speech recorded under very noisy conditions or with a microphone far from the speaker
  * Very spontaneous and overlapping speech

## Training data
Acoustic training data:

| Type                  | Amount (h) |
|-----------------------|:------:|
| Broadcast speech      |   591  |
| Spontaneous speech    |   53   |
| Elderly speech corpus |   53   |
| Talks, lectures       |   49   |
| Parliament speeches   |   31   |
| *Total*               |   *761*  |



## Training procedure

Finetuned using Espnet, and then comverted to transformers format using [this](https://gist.github.com/alumae/2dcf473b667cec9d513b80ea24e94672) script. 
Finetuning procedure is similar to [this](https://huggingface.co/espnet/shihlun_asr_whisper_medium_finetuned_librispeech100) model.
Finetuning was done for 3 epochs, with model averaging at the end of training.

## Evaluation results

### WER

WER results below are obtained using greedy decoding (i.e., beam size 1).

|Dataset | WER |
|---|---|
| Common Voice 8.0 | 11.2 |
| Common Voice 11.0 | 12.0 |
