from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by module/dev_tools/assets_extract.py.
# Don't modify it manually.
class GeneralRoomAssets: 


	# Image Rule Assets
	# description 
	I_CREATE_ROOM = RuleImage(roi_front=(985,600,177,58), roi_back=(396,569,813,100), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_create_room.png")
	# description 
	I_CREATE_ENSURE = RuleImage(roi_front=(813,560,129,63), roi_back=(813,560,129,63), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_create_ensure.png")
	# 勾选不公开的图 
	I_ENSURE_PRIVATE = RuleImage(roi_front=(748,489,36,40), roi_back=(748,489,36,40), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_private.png")
	# 这个是还没勾选的图 
	I_ENSURE_PRIVATE_FALSE = RuleImage(roi_front=(747,489,37,40), roi_back=(747,489,37,40), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_private_false.png")
	# description 
	I_ENSURE_PRIVATE_2 = RuleImage(roi_front=(401,409,34,40), roi_back=(401,409,34,40), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_private_2.png")
	# description 
	I_ENSURE_PRIVATE_FALSE_2 = RuleImage(roi_front=(400,408,36,38), roi_back=(400,408,36,38), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_ensure_private_false_2.png")
	# description 
	I_CREATE_ENSURE_2 = RuleImage(roi_front=(552,489,42,55), roi_back=(552,489,42,55), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_create_ensure_2.png")
	# description 
	I_GR_MATCHING_NEW = RuleImage(roi_front=(62,571,42,121), roi_back=(62,571,42,121), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_gr_matching_new.png")
	# description 
	I_GR_BACK_YELLOW = RuleImage(roi_front=(19,13,53,53), roi_back=(19,13,53,53), threshold=0.8, method="Template matching", file="./tasks/Component/GeneralRoom/gr/gr_gr_back_yellow.png")


