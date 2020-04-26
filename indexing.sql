create index orderpostcode_index on orderr(postalcode);
create index ordercity_index on orderr(city);
create index labcity_index on lab(city);
create index orderruid_index on orderr(uid);
create index deleta_symptoms on delivery(daid,eta);
create index deloid_index on delivery(oid);
create index deloid_index on delivery(daid);
create index delrevdeid_index on deliveryReviews(deid);

create index opslotdateid_index on OpenSlots(SDATE);
create index prescdrid_index on Prescription(drid);
create index prescdid_index on Prescription(did);

create index opslotdid_index on OpenSlots(did);
create index appmtsid_index on Appointment(sid);
create index docRevaid_index on Doctorreviews(aid);
create index DoctorCityIndex on Doctor(city);
create index drugName_index on Drug(Drname);

create index drugscid_index on Drug(cid);
create index orderrdrid_index on Orderr(drid);
create index drugRevoid_index on drugreviews(oid);
create index drugsymp_index on drug(symptoms);
create index drugsick_index on drug(sickness);
create index UserCityIndex on Userr(city);

create index testuid_index on Test(uid);
create index testlabid_index on Test(labid);
create index testtid_index on Test(Tid);
create index labreviewtid_index on labreviews(tid);
create index tdiagrepotid_index on DiagnosticReports(tid);

create index drugid_index on drug(drid);
create index docid_index on doctor(did);
create index delAgid_index on DeliveryAgency(daid);
create index opslotid_index on OpenSlots(sid);
create index compid_index on Company(cid);
create index delArid_index on DeliveryArea(deaid);
create index drugRevid_index on drugreviews(drreid);
create index delid_index on delivery(deid);
create index labid_index on Lab(labid);
create index Labrevid_index on Labreviews(lrid);
create index delrevid_index on deliveryreviews(dereid);
create index orderrid_index on orderr(Oid);
create index testid_index on Test(tid);
create index userrid_index on userr(uid);
create index diagRepid_index on DiagnosticReports(dirid);
create index appmtid_index on Appointment(aid);
create index prescid_index on Prescription(prid);
create index docrevid_index on DoctorReviews(dreid);






