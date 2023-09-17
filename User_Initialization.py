
from taipy.gui import Markdown
from taipy.gui import navigate
data = {}
phone_number = ''
first_name = ''
last_name = ''
age = ''
weight = ''
em_first_name = ''
em_last_name = ''
em_phone_number = ''
Medication = ''
for i in range(100):
    exec(f'dosage_{i} = ""')
    exec(f'timing_{i} = ""')

from taipy import Gui
from csv import writer


def submit_form(state):
    global data
    global Pages1
    x = 1 if data['Medication'] == "" else int(data['Medication'])
    for i in range(x):
        exec(f'data[\'Dose_{i}\'] = state.dosage_{i}')
        exec(f'data[\'Timing_{i}\'] = state.timing_{i}')
    with open('database.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(data.values())
        f_object.close()
    Pages1.stop()


def updateMeds(state):
    pass

def to_next_page(state):
    global data
    global page1
    global Pages1
    data['First_Name'] = state.first_name
    data['Last_Name'] = state.last_name
    data['Phone_Number'] = state.phone_number
    data['Weight'] = state.weight
    data['Age'] = state.age
    data['em_first_name'] = state.em_first_name
    data['em_last_name'] = state.em_last_name
    data['em_phone_number'] = state.em_phone_number
    data['Medication'] = state.Medication
    print('here!')
    print(state.Medication)
    x = 1 if state.Medication == "" else int(state.Medication)

    Pages1.pages = {
  'page1': Markdown(page1),
  'page2': Markdown(page2)
}
    global Next_page
    Next_page = """"""
    print(x)
    for i in range(x):
        exec(f'global dosage_{i}')
        exec(f'dosage_{i} =  ""')
        exec(f'timing_{i} = ""')
        Next_page += f"""
Prescription {i+1}
        
        
Dosage: <|{"{" + f"dosage_{i}" + "}"}|input|>
        
        
Timing: <|{"{" + f"timing_{i}" + "}"}|input|>
        
        
        """
    Next_page += """
    

<|Submit|button|on_action=submit_form|>

    """
    Next_page = str(Next_page)
    print(Next_page)
    Pages1.add_page("page3", Next_page)
    navigate(state, to="page3")



page1 = """
# Sign up
<label for="Language">Choose a language:</label> 
    <select name="language" id="language"> 
        <option value="French">English</option> 
        <option value="English">French</option> 
        <option value="Spanish">Spanish</option> 
        <option value="German">German</option> 
    </select>

First Name: <|{first_name}|input|>


Last Name: <|{last_name}|input|>


Phone Number: <|{phone_number}|input|>


Weight (optional): <|{weight}|input|>


Age (optional): <|{age}|input|>


Number of prescription which you use: <|{Medication}|input|>


#Emergency contact information
First Name: <|{em_first_name}|input|>



Last Name: <|{em_last_name}|input|>


Phone Number: <|{em_phone_number}|input|>







<|Next Page|button|on_action=to_next_page|>

"""
text = "og"
page2 ="""
#This is the next page!
<|{text}|>

"""

# Gui(page).run(use_reloader=True)  # use_reloader=True if you are in development
# print(phone_number)
pages = {
  'page1': Markdown(page1),
  'page2': Markdown(page2)
}
Pages1 = Gui(pages=pages)
Pages1.run()