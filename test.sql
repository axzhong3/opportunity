.print "tables includes:"
.table

-- .print "schema is"
-- .schema

.mode csv
-- .output stdout
-- select MILLISEC,LL_Left_Arm,HL_Activity from S1ADL2dat where LL_Left_Arm="reach" and HL_Activity!="NULL" order by MILLISEC limit 1000;

.output out.csv
select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity!="NULL" or LL_Left_Arm!="NULL" or LL_Left_Arm_Object!="NULL" or LL_Right_Arm!="NULL" or LL_Right_Arm_Object!="NULL" or ML_Both_Arms!="NULL";


.output relaxing.csv
-- select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity=="Relaxing" and (LL_Left_Arm!="NULL" or LL_Left_Arm_Object!="NULL" or LL_Right_Arm!="NULL" or LL_Right_Arm_Object!="NULL" or ML_Both_Arms!="NULL");
select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity=="Relaxing";

.output coffeetime.csv
-- select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity=="Coffeetime" and (LL_Left_Arm!="NULL" or LL_Left_Arm_Object!="NULL" or LL_Right_Arm!="NULL" or LL_Right_Arm_Object!="NULL" or ML_Both_Arms!="NULL");
select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity=="Coffeetime";

.output earlymorning.csv
-- select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity=="Earlymorning" and (LL_Left_Arm!="NULL" or LL_Left_Arm_Object!="NULL" or LL_Right_Arm!="NULL" or LL_Right_Arm_Object!="NULL" or ML_Both_Arms!="NULL");
select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity=="Earlymorning";

.output cleanup.csv
-- select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity=="Cleanup" and (LL_Left_Arm!="NULL" or LL_Left_Arm_Object!="NULL" or LL_Right_Arm!="NULL" or LL_Right_Arm_Object!="NULL" or ML_Both_Arms!="NULL");
select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity=="Cleanup";

.output sandwichtime.csv
-- select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity=="Sandwichtime" and (LL_Left_Arm!="NULL" or LL_Left_Arm_Object!="NULL" or LL_Right_Arm!="NULL" or LL_Right_Arm_Object!="NULL" or ML_Both_Arms!="NULL");
select MILLISEC, Locomotion, HL_Activity, LL_Left_Arm, LL_Left_Arm_Object, LL_Right_Arm, LL_Right_Arm_Object, ML_Both_Arms from S1ADL2dat where HL_Activity=="Sandwichtime";
