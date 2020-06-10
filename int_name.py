## Turns a number into its English name.
#  @param number a poistive integer < 1,000,000,000
#  @return the name of the number (e.g. "two hundred seventy four")
#
def intName(number) :
   name = ""
   part = number

   if part >= 1000000 :
      name = name + intName1000(part // 1000000) + " million "
      part = part % 1000000

   if part >= 1000 :
      name = name + intName1000(part // 1000) + " thousand "
      part = part % 1000

   if part >= 1 :
      name = name + intName1000(part)
      part = part 

   return name

## Turns a number into its English name.
#  @param number a poistive integer < 1,000
#  @return the name of the number (e.g. "two hundred seventy four")
#
def intName1000(number) :
   part = number # The part that still needs to be converted.
   name = ""     # The name of the number.

   if part >= 100 :
      name = digitName(part // 100) + " hundred"
      part = part % 100

   if part >= 20 :
      name = name + " " + tensName(part)
      part = part % 10
   elif part >= 10 :
      name = name + " " + teenName(part)
      part = 0

   if part > 0 :
      name = name + " " + digitName(part)

   return name

## Turns a digit into its English name.
#  @param digit an integer between 1 and 9
#  @return the name of digit ("one" ... "nine")
#
def digitName(digit) :
   if digit == 1: return "One"
   if digit == 2: return "Two"
   if digit == 3: return "Three"
   if digit == 4: return "Four"
   if digit == 5: return "Five"
   if digit == 6: return "Six"
   if digit == 7: return "Seven"
   if digit == 8: return "Eight"
   if digit == 9: return "Nine"
   return ""

## Turns a number between 10 and 19 into its English name.
#  @param number an integer between 10 and 19
#  @return the name of the given number ("ten" ... "nineteen")
#
def teenName(number) :
   if number == 10 : return "Ten"
   if number == 11 : return "Eleven"
   if number == 12 : return "Twelve"
   if number == 13 : return "Thirteen"
   if number == 14 : return "Fourteen"
   if number == 15 : return "Fifteen"
   if number == 16 : return "Sixteen"
   if number == 17 : return "Seventeen"
   if number == 18 : return "Eighteen"
   if number == 19 : return "Nineteen"
   return ""

## Gives the name of the tens part of a number between 20 and 99.
#  @param number an integer between 20 and 99
#  @return the name of the tens part of the number ("twenty" ... "ninety")
#
def tensName(number) :
   if number >= 90 : return "Ninety"
   if number >= 80 : return "Eighty"
   if number >= 70 : return "Seventy"
   if number >= 60 : return "Sixty"
   if number >= 50 : return "Fifty"
   if number >= 40 : return "Forty"
   if number >= 30 : return "Thirty"
   if number >= 20 : return "Twenty"
   return ""
