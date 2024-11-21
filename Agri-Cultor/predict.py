def prediction(lis):
    pred_lis = lis
    mis = [['1','1','1','1','0','2','2'],['1','1','1','1','1','2','1'],['2','1','1','1','1','2','1'],['1','1','1','1','2','2','1'],['2','1','1','1','2','2','1'],['1','1','1','1','3','2','1'],['2','1','1','1','3','2','1'],['1','1','1','1','4','2','1'],['2','1','1','1','4','2','1'],['1','1','1','1','5','2','1'],['2','1','1','1','5','2','1'],['1','1','1','1','6','2','1'],['2','1','1','1','6','2','1'], ['1','2','1','1','1','2','1'],['2','2','1','1','1','2','1'],['1','2','1','1','2','2','1'],['2','2','1','1','2','2','1'],['1','2','1','1','3','2','1'],['2','2','1','1','3','2','1'],['1','2','1','1','4','2','1'],['2','2','1','1','4','2','1'],['1','2','1','1','5','2','1'],['2','2','1','1','5','2','1'],['1','2','1','1','6','2','1'],['2','2','1','1','6','2','1'],    ['1','3','2','2','1','3','3'],['2','3','2','2','1','3','3'],['1','3','2','2','1','3','3'],['2','3','2','2','2','3','3'],['1','3','2','2','3','3','3'],['2','3','2','2','3','3','3'],['1','3','2','2','4','3','3'],['2','3','2','2','4','3','3'],['1','3','2','2','5','3','3'],['2','3','2','2','5','3','3'],['1','3','2','2','6','3','3'],['2','3','2','2','6','3','3'], ['1','4','2','2','1','3','3'],['2','4','2','2','1','3','3'],['1','4','2','2','2','3','3'],['2','4','2','2','2','3','3'],['1','4','2','2','3','3','3'],['2','4','2','2','3','3','3'],['1','4','2','2','4','3','3'],['2','4','2','2','4','3','3'],['1','4','2','2','5','3','3'],['2','4','2','2','5','3','3'],['1','4','2','2','6','3','3'],['2','4','2','2','6','3','3']]
    dis_lis = [
              '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice;
                    • Breakfast(10:00 am):- Seasonal Fruits or Smoothie or Occasional Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                     Note:-;
                      • Maintain this diet plan for 21 days without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;     

                     *****************************  Vegetables and Fruits *****************************;
                    
                    • Vegetables:- Green leafy vegetables, Root Vegetables and Cruciferous Vegetables, Green and Orange Vegetables, Lentils and other pulses;
                    • Fruits:- Citrus fruits, Berries, High-GI fruits, and any Regional and Seasonal fruits; 
                    • Millets:- Barnyard, Amaranth, Little, Kodo, Finger, Pearl, Sorghum, Buckwheat, Foxtail, Browntop ; 
                    • Dry Fruits:- Mix Soaked Dry Fruits;
                    • Seeds:- Chia, Flax, Sunflower, Pumpkin, Watermelon;''',

                '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;      

                     *****************************  Vegetables and Fruits *****************************;
                    
                    • Vegetables:- Beans, Sweet potatoes,  Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus; 
                    • Fruits:- Guava, Citrus fruits, High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Buckwheat, Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Watermelon, Sunflower and Pumpkin;''',            
                

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);

                     Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
    
                    *****************************  Vegetables and Fruits *****************************;
                    
                    • Vegetables:- Green leafy vegetables, Beans, Sweet potatoes,  Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Apricots, Almonds,Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Chia seeds, Flax;''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Lentils, Green leafy vegetables, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Apples, Citrus fruits, Berries, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Foxtail, Little, Kodo, Finger, Pearl; 
                    • Dry Fruits:- Anjeer, Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Watermelon, Sunflower, Chia seeds; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Tomatoes, Zucchini, Asparagus, Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers; 
                    • Fruits:- High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Browntop, Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:-Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Cauliflower, Cabbages, Green leafy vegetables, Beans, Root Vegetables, Peppers, Tomatoes; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Anjeer, Almonds,Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Beets, Celery, Lettuce, Peppers, Green leafy vegetables, Beans, Sweet potatoes, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Mix soaked dry fruits;
                    • Seeds:- Sunflower Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Orange Vegetables; 
                    • Fruits:- Kiwis, Citrus fruits, Berries, High-GI fruits, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Foxtail, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew, Pista ;
                    • Seeds:- Watermelon, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Green leafy vegetables, Beans, Sweet potatoes; 
                    • Fruits:- High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Buckwheat, Kodo, Pearl, Sorghum; 
                    • Dry Fruits:- Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Sunflower, Pumpkin; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Finger, Pearl, Sorghum, Little, Kodo ; 
                    • Dry Fruits:- Mix soaked dry fruits;
                    • Seeds:- Watermelon, Chia Seeds; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Peppers, Tomatoes, Zucchini, Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Foxtail, Pearl, Buckwheat, Kodo; 
                    • Dry Fruits:- Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Watermelon, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green vegetables, Potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini; 
                    • Fruits:- Any Regional and Seasonal fruits; 
                    • Millets:- Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew & mix soaked dry fruits;
                    • Seeds:- Sunflower and Chia seeds; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds, Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Sunflower; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini; 
                    • Fruits:- High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Barnyard, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew, Pista & mix soaked dry fruits;
                    • Seeds:-  Watermelon, Pumpkin, Chia Seeds; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);

                     Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
    
                    *****************************  Vegetables and Fruits *****************************;
                    
                    • Vegetables:- Celery, Cauliflower, Broccoli, Lettuce, Peppers, Tomatoes, Zucchini,; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Barnyard, Barnyard, Kodo, Finger; 
                    • Dry Fruits:- Mix soaked dry fruits;
                    • Seeds:- Watermelon, Chia;''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Carrots, Potatoes, Beets, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew & mix soaked dry fruits;
                    • Seeds:- Flax and Watermelon; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Zucchini, Asparagus, Swiss Chard, Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes; 
                    • Fruits:- Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Amaranth, Little Millet , Barnyard; 
                    • Dry Fruits:- Almonds,Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Lentils and other pulses, Beans, Carrots, Beets, Celery, Lettuce, Peppers, Tomatoes; 
                    • Fruits:- Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Watermelon, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Roundguard, Beans, Sweet potatoes, Beets, Celery, Lettuce, Arugula, Rocket leaves and Kale leaves; 
                    • Fruits:- Pomegranates, Grapes, Oranges, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Barnyard, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Sunflower, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green leafy vegetables, Root Vegetables, Tomatoes, Zucchini; 
                    • Fruits:- Apples, Oranges, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Foxtail, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Mix soaked dry fruits;
                    • Seeds:- Watermelon, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Cabbages, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Watermelon, Oranges, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Walnuts, Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Watermelon seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Tomato, Green leafy vegetables, Beans, Beets, Celery, Lettuce, Peppers; 
                    • Fruits:- Mangoes, Citrus fruits, Berries,High-GI fruits & any Regional and Seasonal fruits; 
                    • Millets:- Barnyard, Foxtail, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Anjeer, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Watermelon, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Potatoes, Carrots, Green leafy vegetables, Beans, Peppers, Tomatoes, Zucchini; 
                    • Fruits:-Apples, Guavas, Oranges, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Foxtail, Barnyard, Pearl, Sorghum; 
                    • Dry Fruits:- Walnuts, Pista & mix soaked dry fruits;
                    • Seeds:- Sunflower, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Beans,Tomatoes, Green and Yellow vegetables ; 
                    • Fruits:- Avocados, Pears & Seasonal fruits; 
                    • Millets:- Barnyard, Foxtail, Little, Kodo; 
                    • Dry Fruits:- Walnuts, Cashew & mix soaked dry fruits;
                    • Seeds:- Sunflower, Watermelon, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Any fresh juice; 
                    • Breakfast(10:00 am):- Smoothie or Smoothie Bowl; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit or smoothie;
                    • Dinner(6:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies);
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                   • Vegetables:- Tomato, Green leafy vegetables, Beans, Beets, Celery, Lettuce, Peppers; 
                    • Fruits:- Mangoes, Citrus fruits, Berries,High-GI fruits & any Regional and Seasonal fruits; 
                    • Millets:- Barnyard, Foxtail, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Anjeer, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Watermelon, Flax; ''',







                   '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Potatoes, Carrots, Green leafy vegetables, Beans, Peppers, Tomatoes, Zucchini; 
                    • Fruits:-Apples, Guavas, Oranges, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Foxtail, Barnyard, Pearl, Sorghum; 
                    • Dry Fruits:- Walnuts, Pista & mix soaked dry fruits;
                    • Seeds:- Sunflower, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;

                     Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
    
                    *****************************  Vegetables and Fruits *****************************;
                    
                    • Vegetables:- Tomato, Green leafy vegetables, Beans, Beets, Celery, Lettuce, Peppers; 
                    • Fruits:- Mangoes, Citrus fruits, Berries,High-GI fruits & any Regional and Seasonal fruits; 
                    • Millets:- Barnyard, Foxtail, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Anjeer, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Watermelon, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Cabbages, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Watermelon, Oranges, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Walnuts, Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Watermelon seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green leafy vegetables, Root Vegetables, Tomatoes, Zucchini; 
                    • Fruits:- Apples, Oranges, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Foxtail, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Mix soaked dry fruits;
                    • Seeds:- Watermelon, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Roundguard, Beans, Sweet potatoes, Beets, Celery, Lettuce, Arugula, Rocket leaves and Kale leaves; 
                    • Fruits:- Pomegranates, Grapes, Oranges, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Barnyard, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Sunflower, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Lentils and other pulses, Beans, Carrots, Beets, Celery, Lettuce, Peppers, Tomatoes; 
                    • Fruits:- Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Watermelon, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Carrots, Potatoes, Beets, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew & mix soaked dry fruits;
                    • Seeds:- Flax and Watermelon; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Celery, Cauliflower, Broccoli, Lettuce, Peppers, Tomatoes, Zucchini,; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Barnyard, Barnyard, Kodo, Finger; 
                    • Dry Fruits:- Mix soaked dry fruits;
                    • Seeds:- Watermelon, Chia;''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini; 
                    • Fruits:- High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Barnyard, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew, Pista & mix soaked dry fruits;
                    • Seeds:-  Watermelon, Pumpkin, Chia Seeds; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds, Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Sunflower; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;

                     Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
    
                    *****************************  Vegetables and Fruits *****************************;
                    
                    • Vegetables:- Green vegetables, Potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini; 
                    • Fruits:- Any Regional and Seasonal fruits; 
                    • Millets:- Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew & mix soaked dry fruits;
                    • Seeds:- Sunflower and Chia seeds; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Peppers, Tomatoes, Zucchini, Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Foxtail, Pearl, Buckwheat, Kodo; 
                    • Dry Fruits:- Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Watermelon, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Finger, Pearl, Sorghum, Little, Kodo ; 
                    • Dry Fruits:- Mix soaked dry fruits;
                    • Seeds:- Watermelon, Chia Seeds; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Green leafy vegetables, Beans, Sweet potatoes; 
                    • Fruits:- High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Buckwheat, Kodo, Pearl, Sorghum; 
                    • Dry Fruits:- Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Sunflower, Pumpkin; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers, Orange Vegetables; 
                    • Fruits:- Kiwis, Citrus fruits, Berries, High-GI fruits, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Foxtail, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Almonds,Cashew, Pista ;
                    • Seeds:- Watermelon, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Beets, Celery, Lettuce, Peppers, Green leafy vegetables, Beans, Sweet potatoes, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Mix soaked dry fruits;
                    • Seeds:- Sunflower Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Cauliflower, Cabbages, Green leafy vegetables, Beans, Root Vegetables, Peppers, Tomatoes; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Anjeer, Almonds,Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Tomatoes, Zucchini, Asparagus, Green leafy vegetables, Beans, Sweet potatoes, Beets, Celery, Lettuce, Peppers; 
                    • Fruits:- High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Browntop, Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:-Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Chia seeds, Flax; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Lentils, Green leafy vegetables, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Apples, Citrus fruits, Berries, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Foxtail, Little, Kodo, Finger, Pearl; 
                    • Dry Fruits:- Anjeer, Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Watermelon, Sunflower, Chia seeds; ''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Green leafy vegetables, Beans, Sweet potatoes,  Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus, Swiss Chard; 
                    • Fruits:- Citrus fruits, Berries,High-GI fruits, & any Regional and Seasonal fruits; 
                    • Millets:- Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Apricots, Almonds,Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Pumpkin, Chia seeds, Flax;''',

                    '''
                    • Pre-Breakfast (8:00 am):- Ash gourd juice or Coconut Water or Vegetable Juice; 
                    • Breakfast(10:00 am):- Any One Seasonal Fruit; 
                    • Lunch(1:00 pm):- Grain Meal(Satvic Roti-Sabzi or any grain with lots of veggies); 
                    • Mid-Meal(4:00 pm):- Any one seasonal fruit if hungry;
                    • Dinner(6:00 pm):- Satvic Salad or Satvic Soup;
                    
                    Note:-;
                      • Maintain this diet plan for 3 months without failure;
                      • Swap your Fragmented foods for Wholesome Foods;
                      • Ex: Replace i)white rice with Brown Rice, Whole grains, Bulgur, Rye, Quinoa, Oatmeal; 
                                   ii) white salt with Pink Himalayan Salt;
                                   iii) white sugar with Jaggery and dates;
                    
                    *****************************  Vegetables and Fruits *****************************;

                    • Vegetables:- Beans, Sweet potatoes,  Beets, Celery, Lettuce, Peppers, Tomatoes, Zucchini, Asparagus; 
                    • Fruits:- Guava, Citrus fruits, High-GI fruits, Avocado, Banana, Kiwis, & any Regional and Seasonal fruits; 
                    • Millets:- Buckwheat, Little, Kodo, Finger, Pearl, Sorghum; 
                    • Dry Fruits:- Cashew, Pista & mix soaked dry fruits;
                    • Seeds:- Watermelon, Sunflower and Pumpkin;''',            
     
    
    
              ]
       
    for i in range(0,len(pred_lis)):
        if mis[i] == pred_lis:
            return dis_lis[i]
    return dis_lis[0]
        
            
    #if mis[0] == lis:
        #return dis_lis[0]