def insert_item(meds, brandname, active, list_generics): ######
    '''
    Modifies dictionary meds to insert an item. The key is brandname, the value is
       a tuple containing 2 elements specified by paramaters active and list-generics
    Parameters: meds: dictionary
       brandname: string. The key 
       active: string. The active components 
       list_generics: list of strings. The generic names for this OC
    Returns: None
    '''
    meds[brandname] = (active, list_generics)
    

def find_active(meds, brandname):  ######
    '''
    Finds the active components of a medication in the dictionary
    Parameters: meds: dictionary
       brandname: string. The key, brand name of the medication 
    Returns: string containing active components if the key is in the dictionary, 
       else returns string "No medication with brand name <brandname>"
    '''
    if brandname in meds:
      return meds[brandname][0]

    else:
      return "No medication with brandname", brandname

def find_ith_value(meds, brandname, i):
    '''
    Finds the ith element of the tuple that is the value of a medication in the dictionary
    Parameters: meds: dictionary
       brandname: string. The key, brand name of the medication
    Returns: string or list containing ith element of value if the key is in the dictionary,
       else returns string "No medication with brand name <brandname>"
	   If there is no ith value of the entry, returns string 
           "No ith value of entry for brand name <brandname>"
    '''
    if brandname in meds and 0 <= i < len(meds[brandname]):
      return meds[brandname][i]

    elif brandname not in meds:
      return "No medication with brandname", brandname

    elif i >= len(meds[brandname]):
      return "no ith value of entry for brand name", brandname       

def add_generic(meds, brandname, generic): # ********************
    '''
    Modifieds meds to adds a new generic to the list of generics for medication brandname. 
       If there is no key for brandname in meds then then meds is not modified
          and an error message is printed to standard output
       If generic is already in brandname's list of generics then meds is not modified
          and an error message is printed to standard output
    Parameters: meds: dictionary
       brandname: string. The key, brand name of the medication 
       generic: string. The name of the generic to add to the list of generics for brandname
    Returns: None
    ''' 
    if brandname in meds and generic not in meds[brandname][1]:
      meds[brandname][1].append(generic)

    elif brandname not in meds:
      print(brandname, "does not exist")

    elif generic in meds[brandname][1]:
      print(generic, " already exists")
  
        
if __name__ == "__main__":        
    drugs = {
    "Demulen 1/35":    ("EE 35 mcg / Ethynodiol diacetate 1 mg", ["Zovia 1/35E", "Kelnor 1/35"]),
    "Yasmin":    ("EE 30 mcg/ Drospirenone 3 mg",  ["Ocella", "Syeda", "Zarah", "Drospirenone/EE"]),
    "Loestrin 1/20": ("EE 20 mcg/ Norethindrone 1 mg", ["Junel 1/20", "Microgestin 1/20", "Gildess 1/20", "Norethindrone/EE"]),
    "Loestrin 1.5/30": ("EE 30 mcg/ Norethindrone 1.5 mg", ["Junel 1.5/30", "Microgestin 1.5/30", "Gildess 1.5/30", "Larin 1.5/30"])
    }

    #print(drugs)
    # insert: "Ovcon-50","EE 50 mcg/ Norethindrone 1 mg", No generics
    insert_item(drugs, "Ovcon-50", "EE 50 mcg/ Norethindrone 1 mg", [])

#    print(drugs)
 #   print()

    # find the active ingredients "Loestrin 1/20"
    print(find_active(drugs, "Loestrin 1/20"))
    print(find_active(drugs, "lslkjdf"))

    # find the zeroth value of "Loestrin 1/20"
    print(find_ith_value(drugs,"Loestrin 1/20", 0))

    # find the twoeth value of "Loestrin 1/20"
    print(find_ith_value(drugs,"Loestrin 1/20", 1))

    print(find_ith_value(drugs, "sdlkfjdskljfsd", 0))

    print(find_ith_value(drugs, "Loestrin 1/20", 2))

    # find the generic list of "Loestrin 1/20"
    print(find_ith_value(drugs, "Loestrin 1/20", 1))

    # find the oneth generic  of "Loestrin 1/20"
    print(drugs["Loestrin 1/20"][1][0])

    # add the generic "Larin 1/20" to "Loestrin 1/20"
    add_generic(drugs, "Loestrin 1/20", "Larin 1/20")
#   print(drugs["Loestrin 1/20"][1])

    # try to add again the generic "Larin 1/20" to "Loestrin 1/20"
    add_generic(drugs, "Loestrin 1/20", "Larin 1/20")
#    print(drugs["Loestrin 1/20"][1])

    # reprint  the generic list of "Loestrin 1/20"
    print(drugs["Loestrin 1/20"][1])

    # try to add generic to non-existing brandname: should result in error message
    add_generic(drugs, "slkdjfsdkjfl", "eeeee")

    print()
 #   print(drugs)
    print()


