# <center>FEC in Python and its practition in ASR</center>
### <center>**Bob Li**</center>
### <center>*China University of Geosciences, China*</center>
#### <center>*unclebobhk@gmail.com*</center>
## <center>**Abstract**</center>

FEC, acronym of **forward error correction**, is a major practice we resort to in the field of simplex-communication. Concretely, it's a pattern that we augment redundancy, ( which is technically named **parity bits**) to the original data generated from certain association with the original. In this experiment, we adopt *Hamming Code* as the parity bits. 

## 1    Introduction
In telecommunication, information theory, and coding theory, forward error correction (FEC) or channel coding is a technique used for controlling errors in data transmission over unreliable or noisy communication channels. The central idea is the sender encodes the message in a redundant way by using an error-correcting code (ECC).

The redundancy allows the receiver to detect a limited number of errors that may occur anywhere in the message, and often to correct these errors without re-transmission. FEC gives the receiver the ability to correct errors without needing a reverse channel to request re-transmission of data, but at the cost of a fixed, higher forward channel bandwidth. FEC is therefore applied in situations where re-transmissions are costly or impossible, such as one-way communication links and when transmitting to multiple receivers in multicast. For example, in the case of a satellite orbiting around Uranus, a re-transmission because of decoding errors can create a delay of 5 hours. FEC information is usually added to mass storage (magnetic, optical and solid state/flash based) devices to enable recovery of corrupted data, is widely used in modems, is used on systems where the primary memory is ECC memory and in broadcast situations, where the receiver do not have capabilities to request retransmission or doing so would induce significant latency.

<p align="center">
  <img src="https://raw.githubusercontent.com/unclebob7/forward-error-correction-with-hamming-code/master/Forward-Error-Correction.gif">
</p>

<center>PIC1 : illustration</center>

## 2    Flowchart
To be specific, our procedures are implemented as follows. First, we implement the truncation sequence to lower the cost of banwidth while assuring that the effect of truncation is not noticable to the holistic audio.Second, we convert float data-type into binary by segregating the original data into sign-bit, integer-bit and decimal-bit. Third, we concatenate the parity bits to the original to introduce redundancy.
And Finally, we simulate the non-optimal channel of communication and introduce errors to the original seuquence of audio. With the completion of all previous steps, FEC is now ready to be testified.

<p align="center">
  <img src="https://raw.githubusercontent.com/unclebob7/forward-error-correction-with-hamming-code/master/procedure.png">
</p>

<center>PIC2 : procedure</center>

## 3    Algorithmic illustration
The most salient problem worth discussing in the simulation of a compromised channel is whether we should choose the pre-test probability or simply the post-test probability?
And the answer is the former for two specific arguemnts : 
> (i) Every variable in specific time domain should be independent.

> (ii) Every selection of time domain is absolutely random.

The algorithmic illustration in **pseudo code** is as follows : 
<p align="center">
  <img src="https://raw.githubusercontent.com/unclebob7/forward-error-correction-with-hamming-code/master/pseudo_code.png">
</p>


<center>PIC3 : algorithmic illustration</center>

## 3    Comparison of audios
The original sample is shown in the flow, purifed as not much high-frequency noise as it is, while we have introduced sample generated with bit-error-rate of 0.213% and 0.418% respectively.Whilt in PIC4 we have used fragments from Martin.L.King's very famous speech for further application.shown intuitively the comparion of pre and post effect of FEC(forward error correction). The post EBR has been visibly repressed significantly.

![INF FEC](https://raw.githubusercontent.com/unclebob7/forward-error-correction-with-hamming-code/master/inf_comp.PNG)
<center>PIC4 : aud:infinity comparison</center>

![MLK FEC](https://raw.githubusercontent.com/unclebob7/forward-error-correction-with-hamming-code/master/mlk_comp.PNG)
<center>PIC5 : aud:MLK comparison</center>

## 3    Further application on ASR
![ASR EG](https://raw.githubusercontent.com/unclebob7/forward-error-correction-with-hamming-code/master/gcp.png)

<center>PIC6 : google cloud platform</center>

A very much salient problem in ASR(automatic speech recognizer) is the BER(bit error rate) introduced by compromised channel, since ACK(acknowledgement) message in the process has been undoubtedly unaffordable and of significant unfeasibility. This is the absolute scenario where FEC comes into power to ensure the quality of *communication*.Here in the demonstration, we use a high-level API running on my GCP(google cloud platform server) to testify whether FEC can essentially improve(ensure) the quality of audio in the field of *speech recognition*.

![ASR EG](https://raw.githubusercontent.com/unclebob7/forward-error-correction-with-hamming-code/master/fec_gradient_ascend.PNG)

<center>PIC7 : ASR demonstration</center>

[1]Charles Wang; Dean Sklar; Diana Johnson (Winter 2001–2002). *"Forward Error-Correction Coding"*

[2] Maunder, Robert (2016). *"Overview of Channel Coding"*
