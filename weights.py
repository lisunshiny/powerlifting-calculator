PLATES = [45, 35, 25, 10, 5, 2.5]
BAR_WEIGHT = 45

def get_plates(weight, plates):
  # print("hi")
  if weight < BAR_WEIGHT:
    return None
  
  remaining_plate_weight = (weight - BAR_WEIGHT) / 2
  plates.sort(reverse = True)
  
  current_plate_idx = 0
  plates_per_side = {}
  # todo figure out if end of plates
  while remaining_plate_weight > 0:
    if current_plate_idx >= len(plates):
      print("cannot do " + str(weight) + ", but heres the plates " + str(plates_per_side) + " for " + str(weight - remaining_plate_weight * 2))
      return plates_per_side
    
    # print("curr idx", current_plate_idx)
    # print("curr plate", plates[current_plate_idx] )
    # print("remaining weight", remaining_plate_weight)

    while plates[current_plate_idx] <= remaining_plate_weight:
      if plates[current_plate_idx] not in plates_per_side:
        plates_per_side[plates[current_plate_idx]] = 0

      plates_per_side[plates[current_plate_idx]] += 1
      remaining_plate_weight -= plates[current_plate_idx]
    current_plate_idx += 1

  return plates_per_side

CLOSEST_INTEGER = 5 # if you have micros, do 2.5

def get_percentage_1rm_plates(one_rm, percentage):

  # print("onerm, perc: " + str(one_rm) + " " + str(percentage))
  target_weight = one_rm * percentage
  closest_five = CLOSEST_INTEGER * round(target_weight/CLOSEST_INTEGER)
  print("~" + str(percentage*100) + "% ~")

  print("For: " + str(closest_five)  + " (" + str(target_weight) + ")")
  # if closest_five != target_weight:
  #   print("need to round to " + str(closest_five)  + " from " + str(target_weight))
  return get_plates(closest_five, PLATES)

def get_percentage_1rm_amt(one_rm, percentage, num):

  # print("onerm, perc: " + str(one_rm) + " " + str(percentage))
  target_weight = one_rm * percentage
  closest_five = CLOSEST_INTEGER * round(target_weight/CLOSEST_INTEGER)
  bar_weight =  (closest_five - BAR_WEIGHT) / 2
  print("~ 1x" + str(num) + " at "+ str(percentage*100) + "% ~")
  print(str(closest_five) + " lbs " + "(" + str("{:.1f}".format(target_weight)) +"): "+ ""+ "")  
  print(str("{:.1f}".format(bar_weight)) + " lbs per side")

  # print("For: " + str(closest_five)  + " (" + str(target_weight) + ")")
  # if closest_five != target_weight:
  #   print("need to round to " + str(closest_five)  + " from " + str(target_weight))
  return bar_weight
  print("")
  pass


# print(get_plates(45, PLATES), 45) # bar only
# print(get_plates(120, PLATES), 120) # uses 2.5
# print(get_plates(95, PLATES)) # duplicate
# print(get_plates(92.5, PLATES)) # duplicate
# print(get_plates(97.5, PLATES)) # duplicate

# print(get_percentage_1rm_plates(105, .7)) 
# print(get_percentage_1rm_plates(105, .75))
# print(get_percentage_1rm_plates(105, .8))
