import os
import glob
from tqdm import tqdm

WORKFLOW = ["unknown", "Marking", "Bosmin_Infusion", "Flap_head", "Flap_tail",
            "Flap_outer", "Flap_inner", "Sentinel_Lymph_Node_Biopsy",
            "Mammary_Gland_Pealing_from_Pectoralis_Major_Muscle",
            "Mammary_Gland_Pealing_from_Surrounding_Tissue", "Cleaning",
            "Drain_Insertion", "Skin_Suture", "Other_moving", "Other_preparation"]

years = ["20170707", "20200214_1", "20200214_2", "20220405", "20220422",
         "20220628", "20220715"]


for wf in WORKFLOW:
    for year in years:
        imgs = glob.glob("../workflow_data/" + wf + "/multitool" + year + "/*.png")
        for img in imgs:
            os.remove(img)

