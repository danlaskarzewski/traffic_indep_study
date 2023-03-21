from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import *
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
import xgboost as xgb
import random
import pandas as pd
import shap
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE 
from collections import Counter

df = pd.read_csv("../3m_Boston_ALL_norm_byDT.csv")
# df = pd.read_csv("../temp_Boston_CrashWeather_byDT.csv")
df_ml = df.fillna(0)

#CrashWeather
# labels = ["MAX_INJR_SVRTY_CL_Fatal injury (K)"]
# df[label] = df['BMICLSCD'].replace(BMI_Codes, dummy_vars)
# features = ["NUMB_NONFATAL_INJR","NUMB_VEHC", "NUM_LANES","OPP_LANES","temperature_2m (°F)","apparent_temperature (°F)","precipitation (inch)","rain (inch)","snowfall (cm)","cloudcover (%)","windspeed_10m (mp/h)","winddirection_10m (°)","windgusts_10m (mp/h)","soil_moisture_0_to_7cm (m³/m³)", "AGE_DRVR_YNGST_75-84", "AGE_DRVR_YNGST_65-74", "AGE_DRVR_YNGST_55-64", "AGE_DRVR_YNGST_45-54", "AGE_DRVR_YNGST_35-44", "AGE_DRVR_YNGST_25-34", "AGE_DRVR_YNGST_21-24", "AGE_DRVR_YNGST_18-20", "AGE_DRVR_YNGST_16-17", "AGE_DRVR_OLDEST_16-17","AGE_DRVR_OLDEST_18-20","AGE_DRVR_OLDEST_21-24","AGE_DRVR_OLDEST_25-34","AGE_DRVR_OLDEST_35-44","AGE_DRVR_OLDEST_45-54","AGE_DRVR_OLDEST_55-64","AGE_DRVR_OLDEST_65-74","AGE_DRVR_OLDEST_75-84","AMBNT_LIGHT_DESCR_Dark - lighted roadway","AMBNT_LIGHT_DESCR_Dark - roadway not lighted","AMBNT_LIGHT_DESCR_Dark - unknown roadway lighting","AMBNT_LIGHT_DESCR_Dawn","AMBNT_LIGHT_DESCR_Daylight","AMBNT_LIGHT_DESCR_Dusk","AMBNT_LIGHT_DESCR_Not reported","AMBNT_LIGHT_DESCR_Other","AMBNT_LIGHT_DESCR_Unknown","ROAD_SURF_COND_DESCR_Dry","ROAD_SURF_COND_DESCR_Ice","ROAD_SURF_COND_DESCR_Not reported","ROAD_SURF_COND_DESCR_Other","ROAD_SURF_COND_DESCR_Sand, mud, dirt, oil, gravel","ROAD_SURF_COND_DESCR_Slush","ROAD_SURF_COND_DESCR_Snow","ROAD_SURF_COND_DESCR_Unknown","ROAD_SURF_COND_DESCR_Water (standing, moving)","ROAD_SURF_COND_DESCR_Wet","RDWY_JNCT_TYPE_DESCR_Driveway","RDWY_JNCT_TYPE_DESCR_Five-point or more","RDWY_JNCT_TYPE_DESCR_Four-way intersection","RDWY_JNCT_TYPE_DESCR_Not at junction","RDWY_JNCT_TYPE_DESCR_Not reported","RDWY_JNCT_TYPE_DESCR_Off-ramp","RDWY_JNCT_TYPE_DESCR_On-ramp","RDWY_JNCT_TYPE_DESCR_Railway grade crossing","RDWY_JNCT_TYPE_DESCR_T-intersection","RDWY_JNCT_TYPE_DESCR_Traffic circle","RDWY_JNCT_TYPE_DESCR_Unknown","RDWY_JNCT_TYPE_DESCR_Y-intersection","TRAFY_DESCR_DESCR_Not reported","TRAFY_DESCR_DESCR_One-way, not divided","TRAFY_DESCR_DESCR_Two-way, divided, positive median barrier","TRAFY_DESCR_DESCR_Two-way, divided, unprotected median","TRAFY_DESCR_DESCR_Two-way, not divided","TRAFY_DESCR_DESCR_Unknown","F_F_CLASS_Interstate","F_F_CLASS_Local","F_F_CLASS_Major Collector","F_F_CLASS_Minor Arterial","F_F_CLASS_Principal Arterial - Other","F_F_CLASS_Principal Arterial - Other Freeways and Expressways","F_F_CLASS_Principal Arterial - Other Freeways or Expressways","FACILITY_Collector - Distributor","FACILITY_Doubledeck","FACILITY_Mainline roadway","FACILITY_Ramp - SB/WB","FACILITY_Rotary","FACILITY_Simple Ramp - Tunnel","FACILITY_Simple Ramp/ Channelized Turning Lane","FACILITY_Simple ramp","FACILITY_Tunnel","month","hour"]

#All
# label = "Red_70088_Late" 
labels = ["Blue_70059_Late","Blue_70038_Late","Green-B_70154_Late","Green-C_70154_Late","Green-D_70154_Late","Green-E_70154_Late","Green-B_70210_Late","Green-C_70210_Late","Green-D_70210_Late","Green-E_70210_Late","Red_70088_Late","Red_70063_Late","Orange_70003_Late","Orange_70034_Late"]
features = ["NUMB_NONFATAL_INJR","NUMB_FATAL_INJR","NUMB_VEHC", "NUM_LANES","OPP_LANES","temperature_2m (°F)","apparent_temperature (°F)","precipitation (inch)","rain (inch)","snowfall (cm)","cloudcover (%)","windspeed_10m (mp/h)","winddirection_10m (°)","windgusts_10m (mp/h)","soil_moisture_0_to_7cm (m³/m³)", "AGE_DRVR_YNGST_75-84", "AGE_DRVR_YNGST_65-74", "AGE_DRVR_YNGST_55-64", "AGE_DRVR_YNGST_45-54", "AGE_DRVR_YNGST_35-44", "AGE_DRVR_YNGST_25-34", "AGE_DRVR_YNGST_21-24", "AGE_DRVR_YNGST_18-20", "AGE_DRVR_YNGST_16-17", "AGE_DRVR_OLDEST_16-17","AGE_DRVR_OLDEST_18-20","AGE_DRVR_OLDEST_21-24","AGE_DRVR_OLDEST_25-34","AGE_DRVR_OLDEST_35-44","AGE_DRVR_OLDEST_45-54","AGE_DRVR_OLDEST_55-64","AGE_DRVR_OLDEST_65-74","AGE_DRVR_OLDEST_75-84", "MAX_INJR_SVRTY_CL_Deceased not caused by crash","MAX_INJR_SVRTY_CL_Fatal injury (K)","MAX_INJR_SVRTY_CL_No Apparent Injury (O)","MAX_INJR_SVRTY_CL_No injury","MAX_INJR_SVRTY_CL_Non-fatal injury - Incapacitating","MAX_INJR_SVRTY_CL_Non-fatal injury - Non-incapacitating","MAX_INJR_SVRTY_CL_Non-fatal injury - Possible","MAX_INJR_SVRTY_CL_Not Applicable","MAX_INJR_SVRTY_CL_Not reported","MAX_INJR_SVRTY_CL_Possible Injury (C)","MAX_INJR_SVRTY_CL_Suspected Minor Injury (B)","MAX_INJR_SVRTY_CL_Suspected Serious Injury (A)","MAX_INJR_SVRTY_CL_Unknown","AMBNT_LIGHT_DESCR_Dark - lighted roadway","AMBNT_LIGHT_DESCR_Dark - roadway not lighted","AMBNT_LIGHT_DESCR_Dark - unknown roadway lighting","AMBNT_LIGHT_DESCR_Dawn","AMBNT_LIGHT_DESCR_Daylight","AMBNT_LIGHT_DESCR_Dusk","AMBNT_LIGHT_DESCR_Not reported","AMBNT_LIGHT_DESCR_Other","AMBNT_LIGHT_DESCR_Unknown","ROAD_SURF_COND_DESCR_Dry","ROAD_SURF_COND_DESCR_Ice","ROAD_SURF_COND_DESCR_Not reported","ROAD_SURF_COND_DESCR_Other","mud_dirt_ROAD_SURF_COND_DESCR_Sand","ROAD_SURF_COND_DESCR_Slush","ROAD_SURF_COND_DESCR_Snow","ROAD_SURF_COND_DESCR_Unknown","ROAD_SURF_COND_DESCR_Water (standing, moving)","ROAD_SURF_COND_DESCR_Wet","RDWY_JNCT_TYPE_DESCR_Driveway","RDWY_JNCT_TYPE_DESCR_Five-point or more","RDWY_JNCT_TYPE_DESCR_Four-way intersection","RDWY_JNCT_TYPE_DESCR_Not at junction","RDWY_JNCT_TYPE_DESCR_Not reported","RDWY_JNCT_TYPE_DESCR_Off-ramp","RDWY_JNCT_TYPE_DESCR_On-ramp","RDWY_JNCT_TYPE_DESCR_Railway grade crossing","RDWY_JNCT_TYPE_DESCR_T-intersection","RDWY_JNCT_TYPE_DESCR_Traffic circle","RDWY_JNCT_TYPE_DESCR_Unknown","RDWY_JNCT_TYPE_DESCR_Y-intersection","TRAFY_DESCR_DESCR_Not reported","TRAFY_DESCR_DESCR_One-way, not divided","divided_positive median barrier_TRAFY_DESCR_DESCR_Two-way","divided_unprotected median_TRAFY_DESCR_DESCR_Two-way","TRAFY_DESCR_DESCR_Two-way, not divided","TRAFY_DESCR_DESCR_Unknown","F_F_CLASS_Interstate","F_F_CLASS_Local","F_F_CLASS_Major Collector","F_F_CLASS_Minor Arterial","F_F_CLASS_Principal Arterial - Other","F_F_CLASS_Principal Arterial - Other Freeways and Expressways","F_F_CLASS_Principal Arterial - Other Freeways or Expressways","FACILITY_Collector - Distributor","FACILITY_Doubledeck","FACILITY_Mainline roadway","FACILITY_Ramp - SB/WB","FACILITY_Rotary","FACILITY_Simple Ramp - Tunnel","FACILITY_Simple Ramp/ Channelized Turning Lane","FACILITY_Simple ramp","FACILITY_Tunnel","month","hour", "Blue_70038_num_trips","Blue_70059_num_trips","Green-B_70154_num_trips","Green-B_70210_num_trips","Green-C_70154_num_trips","Green-C_70210_num_trips","Green-D_70154_num_trips","Green-D_70210_num_trips","Green-E_70154_num_trips","Green-E_70210_num_trips","Orange_70003_num_trips","Orange_70034_num_trips","Red_70063_num_trips","Red_70088_num_trips"]
all_shaps = []

VariablesToOneHot=[]

for f in VariablesToOneHot:
    one_hot = pd.get_dummies(df[f])
    one_hot = one_hot.add_prefix(f+"_")
    # print(one_hot)
    features = features + one_hot.columns.tolist()
    df = df.join(one_hot)
    
#fix Results from Run to run for ease of writing up
random.seed(10)

for l in range (0, len(labels)):
    label = labels[l]

    classifiers = [DummyClassifier(strategy='stratified') , RandomForestClassifier(n_estimators = 100), xgb.XGBClassifier() ]

    k = 4
    resList = []
    for iter_num, fold_indices in enumerate(KFold(n_splits=k, shuffle=True,random_state=10).split(X=df_ml)):

        # Get Instances for Fold
        train_indices = fold_indices[0]
        test_indices = fold_indices[1]
        train_inst = df_ml.iloc[train_indices].copy()
        test_inst = df_ml.iloc[test_indices].copy()

        # oversampling
        counter = Counter(df_ml[label])
        # print(counter)
        oversample = SMOTE()
        oversample =SMOTE(k_neighbors=1)
        # print(df_ml[features])
        X, y = oversample.fit_resample(train_inst[features], train_inst[label])
        # print(X)
        train_inst[features] = X
        train_inst[label] = y

        for clf in classifiers:
            resDict= {}
            #Descriptive Data for Fold
            resDict["NumFeatures"] = len(features)
            resDict["Label"] = label
            resDict["Fold"] = iter_num
            resDict["Classifier"] = str(clf.__class__.__name__)

            #Train Classifier
            clf.fit(train_inst[features], train_inst[label])

            #Evaluate on Test Set
            acc = clf.score(test_inst[features], test_inst[label])

            preds = clf.predict(test_inst[features])
            preds2 = pd.DataFrame(preds)
            preds2.to_csv("preds.csv")
            
            probabilities = clf.predict_proba(test_inst[features])
            df_prob = pd.DataFrame(probabilities, columns=["P0", "P1"], index=test_inst.index)
            ground_truth = test_inst[label].copy()

            resDict["Accuracy"] = acc
            resDict["Precision"] = precision_score(ground_truth, preds)
            resDict["Recall"] = recall_score(ground_truth, preds)
            try:
                resDict["AUROC"] = roc_auc_score(ground_truth, df_prob["P1"])
            except: 
                pass
            resList.append(resDict)
            
            #SHAP
            clf = xgb.XGBClassifier()

            #Retrain on all Data
            clf.fit(df_ml[features],df_ml[label])

            explainer = shap.TreeExplainer(clf)
            fnames = list(features)
            shap_values = explainer.shap_values(df_ml[features])
            all_shaps.append(shap_values)
            # print(shap_values)
            # f1 = plt.figure()

    resultsFrame=pd.DataFrame(resList)
    resultsFrame.to_csv("ML_Results/ML_Results_Raw_" + str(l)+".csv")


shap.summary_plot(all_shaps, features=df_ml[features], feature_names=fnames, show=False)
plt.savefig("ML_Results/SHAPPlot_3m_Full.png")
    # plt.show()