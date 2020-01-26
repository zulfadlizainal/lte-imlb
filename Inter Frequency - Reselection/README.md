# Inter Frequency Load Balancing Simulation - Through Reselection

This simulator will help to simulate Inter Frequency reselection between 2 LTE bands. It will provide distribution understanding of reselection based on priority level according to input parameter (3GPP ASN SIB1, SIB3, and SIB5). The RF measurement metrics info is needed for both band in order for this simulator to work.

### Explanation
In LTE, reselection to other inter frequency band is handled using priority band mechanism. Below are simplified formula for easy understanding.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Explain_Formula.png" alt="Formula" title="Formula" width=100% height=100% />
<br />
Priority: Each band can set own cell priority and the priority to other band.
<br />
Measure: Serving band start to measure the other band.
<br />
Decision: UE start to move (reselect) from serving band to other band.
<br />
<br />
The parameter from the formula can be extracted form network parameters (3GPP ASN SIB1, SIB3, and SIB5). Below are sample for this simulation result.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Explain_Param.png" alt="SIB Parameters" title="SIB Parameters" width=100% height=100% />
<br />
<br />

### 3GPP Specs

Reference from 3GPP, 36.304. Starts from.. chapter 5.
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Explain_3GPP.png" alt="Reference" title="Reference" width=100% height=100% />
<br />
<br />

### Running The Program

There are few steps you need to do to run this simulator. Generally:
<br />
<br />
1. Update parameter <'Input_Parameter.xlsx'>
2. Update measurement data <'Input_Data.xlsx'>
3. Run the code <'Idle_InterFreq_LB.py'>
<br />
<br />
Overall File Structure
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Explain_FileStructure.png" alt="File" title="File" width=100% height=100% />
<br />
<br />
Update parameter <'Input_Parameter.xlsx'>
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Explain_UpdateParam.png" alt="Update Param" title="Update Param" width=100% height=100% />
<br />
<br />
Update measurement data <'Input_Data.xlsx'>
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Explain_UpdateData.png" alt="Update Data" title="Update Data" width=100% height=100% />
<br />
<br />
Run the code <'Idle_InterFreq_LB.py'>
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Explain_RunCode.png" alt="Run Code" title="Run Code" width=100% height=100% />
<br />
<br />
Result
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Result_Equal.png" alt="Equal" title="Equal" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Result_LowtoHigh.png" alt="LowtoHigh" title="LowtoHigh" width=100% height=100% />
<br />
<br />
<img src="https://github.com/zulfadlizainal/4G-LTE-Idle-Mode-Load-Balance/blob/master/img/IFLB_Result_HightoLow.png" alt="HightoLow" title="HightoLow" width=100% height=100% />
<br />
<br />
