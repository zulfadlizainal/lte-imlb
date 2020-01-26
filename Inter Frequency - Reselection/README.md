# Inter Frequency Load Balancing Simulation - Through Reselection

This simulator will help to simulate Inter Frequency reselection between 2 LTE bands. It will provide distribution understanding of reselection based on priority level according to input parameter (3GPP ASN SIB1, SIB3, and SIB5). The RF measurement metrics info is needed for both band in order for this simulator to work.

### Explanation
In LTE, reselection to other inter frequency band is handled using priority band mechanism. Below are simplified formula for easy understanding.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Explain_Formula.png" alt="Formula" title="Formula" width=100% height=100% />
<br />
<br />
The parameter from the formula can be extracted form network parameters (3GPP ASN SIB1, SIB3, and SIB5). Below are sample for this simulation result.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Explain_Param.png" alt="SIB Parameters" title="SIB Parameters" width=100% height=100% />
<br />
<br />

### 3GPP Specs

3GPP 36.213 Sec 5.2.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain07.png" alt="Reference" title="Reference" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain08.png" alt="Reference" title="Reference" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Explain09.png" alt="Reference" title="Reference" width=100% height=100% />
<br />
<br />

### Running The Program

Expected results based on given input. The program will calculate Ideal RS Power Settings based on BW and Power per Antenna Port for every 100% Power Utilization Pa-Pb combination.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Result01.png" alt="Input" title="Input" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Result5MHz_3.png" alt="5MHz" title="5MHz" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Result10MHz_3.png" alt="10MHz" title="10MHz" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-DL-Power-Allocation/blob/master/img/IdealRS_Result20MHz_3.png" alt="20MHz" title="20MHz" width=100% height=100% />
<br />
<br />
