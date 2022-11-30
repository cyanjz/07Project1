import Dataprepare

bi = r'C:\workplace\SW_academy\project1\Data\1bed_img'
bl = r'C:\workplace\SW_academy\project1\Data\1bed_label'
ci = r'C:\workplace\SW_academy\project1\Data\1chair_img'
cl = r'C:\workplace\SW_academy\project1\Data\1chair_label'

save_root = r'C:\workplace\SW_academy\project1\Src'

Dataprepare.bed_chair_together(bi, ci, bl, cl, save_root, cf=Dataprepare.chair_cls_p24)