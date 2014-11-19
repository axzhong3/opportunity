.print "tables includes:"
.table

-- .print "schema is"
-- .schema

.mode csv
.output stdout
select MILLISEC,LL_Left_Arm,HL_Activity from S1ADL2dat where LL_Left_Arm="reach" and HL_Activity!="NULL" order by MILLISEC limit 1000;

.output out.csv
select MILLISEC,LL_Left_Arm,HL_Activity from S1ADL2dat where LL_Left_Arm="reach" and HL_Activity!="NULL" order by MILLISEC limit 1000;
