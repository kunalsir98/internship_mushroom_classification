## Mushroom classification iNEURON INTERNSHIP
DEPLOYEMENT- I HAVE NOT DEPLOYED TO ANY PLATFORM IT IS IN MY LOCAL MACHINE

DOCUMENTATION

1)HIGH LEVEL DOCUMENT (HLD) =  https://drive.google.com/file/d/1GfTkEpaL-OxAzfBOIGVueOhjq0jB-z_r/view?usp=sharing

2)LOW LEVEL DOCUMENT (LLD) = https://drive.google.com/file/d/1xSIxt6bVvLfdrnJ6YWtIwMYoSlUv29BF/view?usp=sharing

3)Architecture = https://drive.google.com/file/d/1uRa07JHzOsxw8Ryl2W6ULm3BX_q4nVZP/view?usp=sharing

4)Wireframe Document =https://drive.google.com/file/d/135Hz99iDAAiaeOX90Jj8NYozn0vAKJbL/view?usp=sharing

5)Detailed Project Report (DPR)= https://drive.google.com/file/d/1X9146s3fV1hxH2HD05zpFmVU3ZScuM9N/view?usp=sharing

ABSTRACT : Mushrooms have been consumed since earliest history. The word Mushroom is derived from the French word for Fungi and Mold. Now-a-days, Mushroom are popular valuable food because they are low in calories, carbohydrate, Fat, sodium and also cholesterol free. Besides this, Mushroom provides important nutrients, including selenium, potassium, riboflavin, niacin, Vitamin D, proteins and fiber. All together with a long history as food source. Mushroom are important for their healing capacity and properties in traditional medicine. It has reported beneficial effects for health and treatment of some disease. Many nutraceutical properties are described in Mushroom like cancer and antitumor attributes. Mushroom act as antibacterial, immune system enhancer and cholesterol lowering Agent. Additionally, they are important source of bio-active compounds. This work is a machine learning model that classifies mushrooms into 2 classes: Poisonous and Edible depending on the features of the mushroom. During this machine learning implementation, we are going to see which features are important to predict whether a mushroom is poisonous or edible.

Problem Statement : The Audubon Society Field Guide to North American Mushrooms contains descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom (1981). Each species is labelled as either definitely edible, definitely poisonous, or maybe edible but not recommended. This last category was merged with the toxic category. The Guide asserts unequivocally that there is no simple rule for judging a mushroom's edibility, such as "leaflets three, leave it be" for Poisonous Oak and Ivy.

The main goal is to predict which mushroom is poisonous & which is edible.

![alt text](image.png)

INTERFACE
![alt text](<Screenshot (175).png>)


ARCHITECTURE
![alt text](<Screenshot (178).png>)


SUMMARY
Summary: Indicates whether the mushroom's flesh changes color when damaged.
Explanation: Some mushrooms change color when bruised or damaged. This characteristic can be important for identifying certain species. For example, some mushrooms may turn blue, red, or brown when handled.
Gill-spacing:

Summary: Describes the distance between the gills on the underside of the mushroom cap.
Explanation: The gill spacing can be close, crowded, or distant. This feature helps in distinguishing between different types of mushrooms, as the arrangement and spacing of gills vary among species.
Gill-size:

Summary: Describes whether the gills are broad or narrow.
Explanation: The size of the gills can be an identifying feature, with some mushrooms having very narrow gills and others having broad gills. This characteristic is used in conjunction with other features to accurately identify the mushroom.
Gill-color:

Summary: Indicates the color of the gills on the underside of the mushroom cap.
Explanation: The color of the gills can range widely, including white, yellow, brown, black, or other colors. This feature is often crucial for identification, as the gill color can change with age or spore production.
Stalk-root:

Summary: Describes the shape and type of the mushroom's stalk base.
Explanation: The base of the mushroom's stalk (stipe) can have different forms, such as bulbous, equal, or rooted. The shape and presence of specific structures at the stalk base are key identification points.
Ring-type:

Summary: Indicates the type and presence of a ring around the mushroom stalk.
Explanation: Some mushrooms have a ring (annulus) on their stalk, which can be persistent or fleeting. The ring can have various forms, such as pendant, evanescent, or large. This is an important identifying feature.
Spore-print-color:

Summary: Refers to the color of the spore print, obtained by placing the mushroom cap gills-down on a surface.
Explanation: The color of the spores, as seen in the spore print, helps in identifying the mushroom. Spore print colors can include white, black, brown, purple, and other shades. This characteristic is often definitive in mushroom identification.
The target column has two class Edible and poisonous 
The first field in app Bruises consist of two option yes and no
The second field in app Gill spacing consist of two option close and crowded
The Third field in app Gill size consist of two option Narrow and Broad
The fourth field in app Gill colour consist of four option Black, Brown, Gray and pink
The fifth field in app Stalk root consist of two option Equal and club
The sixth field in app Ring type consist of two option pendant Evanescent
The seventh field in app spore print colour has three option Black, Brown and white 
The Logistic Regression Classifier model has 100% accuracy on both training data and test data.

