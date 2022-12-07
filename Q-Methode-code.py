########################################
# Import libraries
########################################
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Q-Methodology", page_icon="🥑",layout="wide")

if 'language' not in st.session_state:
    st.session_state['language'] = 'English'
with st.sidebar:
    st.session_state['language'] = st.radio('Select a language',('English','Deutsch'),horizontal=True)



########################################
# Read Data
########################################
df_policies_colnames=['No.','Policy','Policies Deutsch','Benefits','Risks']

df_policies= pd.read_csv("data/All_Food_Loss_Policies.csv", delimiter=';')

if st.session_state['language'] == 'English':
    policy_column='Policy'
else:
    policy_column='Policies Deutsch'

all_policies=df_policies[policy_column].unique()

#shuffle policies
if 'shuffle_seed' not in st.session_state:
    st.session_state['shuffle_seed'] = np.random.randint(0, 100000) 

np.random.seed(st.session_state['shuffle_seed']) 
np.random.shuffle(all_policies)


try:
    len(policies_LPI1)
except:
    policies_LPI1=all_policies

try:
    len(policies_LPI2)
except:
    policies_LPI2=all_policies

try:
    len(policies_LPI3)
except:
    policies_LPI3=all_policies

try:
    len(policies_LPI4)
except:
    policies_LPI4=all_policies

try:
    len(policies_LPI5)
except:
    policies_LPI5=all_policies

try:
    len(policies_LPI6)
except:
    policies_LPI6=all_policies


########################################
# Create Q-Methodology selection
########################################

if st.session_state['language'] == 'English': 
    st.title('Sorting of policies to improve logistics performance')
else: 
    st.title('Zuordung von Policy-Maßnahmen zur Verbesserung der Logistik Performance')

LinkedIn_Link='https://www.linkedin.com/in/jannik-sch%C3%A4ffer'

FAO_Link='https://www.fao.org/platform-food-loss-waste/flw-data/en/'


if st.session_state['language'] == 'English': 
    st.markdown(''' You are invited to participate this Q-methode survey!  
                    The objective of the study is to identify suitable **logistic policies to reduce food loss** around the world. 
                    Therefore an attempt is made to relate losgistics performance and related policy-measures to the FAO [Food Loss and Waste-Database](%s).'''%FAO_Link)
    st.markdown('''The study is being conducted by *[Jannik Schäffer](%s)*.'''%LinkedIn_Link)
else:
    st.markdown(''' Ziel der Studie ist es, geeignete logistische Maßnahmen zur Verringerung der Lebensmittelverluste in der Welt zu ermitteln. 
                    Daher wird versucht, die Logistikleistung und die damit verbundenen politischen Maßnahmen mit den Zahlen der [FAO-Datenbank 
                    für Lebensmittelverluste und -abfälle](%s) in Beziehung zu setzen.'''%FAO_Link)
    st.markdown(''' Die Studie wird durchgeführt von *[Jannik Schäffer](%s)*.'''%LinkedIn_Link)

st.markdown('''---''') 
LPI_Link='https://lpi.worldbank.org/'
LPI_categories_Link='https://lpi.worldbank.org/international'

if st.session_state['language'] == 'English': 
    st.subheader('Introduction')
    st.markdown('''Participation in this survey is voluntary and will take you up to **45 min**.''')
    st.markdown('''**Your Task:** 50 policies should be ranked in ascending order of their potential to improve logistics performance in any category.''')
    with st.expander('**Click to see all available policies**') :
        st.dataframe(all_policies)
    st.markdown('''Each of the following **6 categories** is one of the dimensions on which the World Bank's [Logistics Performance Index](%s) is based.'''%LPI_Link)
    st.markdown('''**Note:** Don't forget to **SAVE** and **SEND** your entries.''')
else:
    st.subheader('Einführung')
    st.markdown('''Eine Teilnahme an dieser Umfrage ist freiwillig und kann in Summe bis zu **45 min** dauern.''')
    st.markdown('''**Ihr Aufgabe:** 50 Policies sollen ihrem Potenzial zur Verbesserung der Logistik-Performance in etwaigen Kategorie aufsteigend geordnet werden.''')
    with st.expander('**Klicken um alle Policy-Maßnahmen einzusehen**') :
        st.dataframe(all_policies)
    st.markdown('''Jede der folgenden **6 Kategorien** ist eine der Dimensionen, auf denen der [Logistics Performance Index](%s) der Weltbank basiert.'''%LPI_Link)
    st.markdown('''**Info:** Vergessen Sie nicht ihre Eingaben zu **SPEICHERN** und anschließend zu **SENDEN**.''')

st.markdown('''---''')   

df_results=pd.DataFrame(columns=['policies','score','LPI-categorie'])
def create_column_content(number_of_items, level_of_agreeness, list_of_options):
    list_of_selected_policies=pd.DataFrame(columns=['policies','score'])
    list_of_selected_policies['policies']=st.multiselect(f'Impact on {LPI_cat}:{level_of_agreeness}',options=list_of_options,max_selections=number_of_items)
    list_of_selected_policies['score']=level_of_agreeness
    list_of_selected_policies['LPI-categorie']=LPI_cat
    return list_of_selected_policies

#####################################
#initiate session state
#####################################
# Initialization
if 'single_completion_check' not in st.session_state:
    st.session_state['single_completion_check'] = 'not started'

if 'customs_completion_check' not in st.session_state:
    st.session_state['customs_completion_check'] = 0
if 'infrastructure_completion_check' not in st.session_state:
    st.session_state['infrastructure_completion_check'] = 0
if 'international_shipments_completion_check' not in st.session_state:
    st.session_state['international_shipments_completion_check'] = 0
if 'logistics_competences_completion_check' not in st.session_state:
    st.session_state['logistics_competences_completion_check'] = 0
if 'tracking_tracing_completion_check' not in st.session_state:
    st.session_state['tracking_tracing_completion_check'] = 0
if 'timeliness_completion_check' not in st.session_state:
    st.session_state['timeliness_completion_check'] = 0

if 'customs1_completion_check' not in st.session_state:
    st.session_state['customs1_completion_check'] = 0
if 'customs2_completion_check' not in st.session_state:
    st.session_state['customs2_completion_check'] = 0
if 'customs3_completion_check' not in st.session_state:
    st.session_state['customs3_completion_check'] = 0
if 'customs4_completion_check' not in st.session_state:
    st.session_state['customs4_completion_check'] = 0
if 'customs5_completion_check' not in st.session_state:
    st.session_state['customs5_completion_check'] = 0
if 'customs6_completion_check' not in st.session_state:
    st.session_state['customs6_completion_check'] = 0
if 'customs7_completion_check' not in st.session_state:
    st.session_state['customs7_completion_check'] = 0
if 'customs8_completion_check' not in st.session_state:
    st.session_state['customs8_completion_check'] = 0
if 'customs9_completion_check' not in st.session_state:
    st.session_state['customs9_completion_check'] = 0

if 'infrastructure1_completion_check' not in st.session_state:
    st.session_state['infrastructure1_completion_check'] = 0
if 'infrastructure2_completion_check' not in st.session_state:
    st.session_state['infrastructure2_completion_check'] = 0
if 'infrastructure3_completion_check' not in st.session_state:
    st.session_state['infrastructure3_completion_check'] = 0
if 'infrastructure4_completion_check' not in st.session_state:
    st.session_state['infrastructure4_completion_check'] = 0
if 'infrastructure5_completion_check' not in st.session_state:
    st.session_state['infrastructure5_completion_check'] = 0
if 'infrastructure6_completion_check' not in st.session_state:
    st.session_state['infrastructure6_completion_check'] = 0
if 'infrastructure7_completion_check' not in st.session_state:
    st.session_state['infrastructure7_completion_check'] = 0
if 'infrastructure8_completion_check' not in st.session_state:
    st.session_state['infrastructure8_completion_check'] = 0
if 'infrastructure9_completion_check' not in st.session_state:
    st.session_state['infrastructure9_completion_check'] = 0

if 'international_shipments1_completion_check' not in st.session_state:
    st.session_state['international_shipments1_completion_check'] = 0
if 'international_shipments2_completion_check' not in st.session_state:
    st.session_state['international_shipments2_completion_check'] = 0
if 'international_shipments3_completion_check' not in st.session_state:
    st.session_state['international_shipments3_completion_check'] = 0
if 'international_shipments4_completion_check' not in st.session_state:
    st.session_state['international_shipments4_completion_check'] = 0
if 'international_shipments5_completion_check' not in st.session_state:
    st.session_state['international_shipments5_completion_check'] = 0
if 'international_shipments6_completion_check' not in st.session_state:
    st.session_state['international_shipments6_completion_check'] = 0
if 'international_shipments7_c0ompletion_check' not in st.session_state:
    st.session_state['international_shipments7_completion_check'] = 0
if 'international_shipments8_completion_check' not in st.session_state:
    st.session_state['international_shipments8_completion_check'] = 0
if 'international_shipments9_completion_check' not in st.session_state:
    st.session_state['international_shipments9_completion_check'] = 0

if 'logistics_competences1_completion_check' not in st.session_state:
    st.session_state['logistics_competences1_completion_check'] = 0
if 'logistics_competences2_completion_check' not in st.session_state:
    st.session_state['logistics_competences2_completion_check'] = 0
if 'logistics_competences3_completion_check' not in st.session_state:
    st.session_state['logistics_competences3_completion_check'] = 0
if 'logistics_competences4_completion_check' not in st.session_state:
    st.session_state['logistics_competences4_completion_check'] = 0
if 'logistics_competences5_completion_check' not in st.session_state:
    st.session_state['logistics_competences5_completion_check'] = 0
if 'logistics_competences6_completion_check' not in st.session_state:
    st.session_state['logistics_competences6_completion_check'] = 0
if 'logistics_competences7_completion_check' not in st.session_state:
    st.session_state['logistics_competences7_completion_check'] = 0
if 'logistics_competences8_completion_check' not in st.session_state:
    st.session_state['logistics_competences8_completion_check'] = 0
if 'logistics_competences9_completion_check' not in st.session_state:
    st.session_state['logistics_competences9_completion_check'] = 0

if 'tracking_tracing1_completion_check' not in st.session_state:
    st.session_state['tracking_tracing1_completion_check'] = 0
if 'tracking_tracing2_completion_check' not in st.session_state:
    st.session_state['tracking_tracing2_completion_check'] = 0
if 'tracking_tracing3_completion_check' not in st.session_state:
    st.session_state['tracking_tracing3_completion_check'] = 0
if 'tracking_tracing4_completion_check' not in st.session_state:
    st.session_state['tracking_tracing4_completion_check'] = 0
if 'tracking_tracing5_completion_check' not in st.session_state:
    st.session_state['tracking_tracing5_completion_check'] = 0
if 'tracking_tracing6_completion_check' not in st.session_state:
    st.session_state['tracking_tracing6_completion_check'] = 0
if 'tracking_tracing7_completion_check' not in st.session_state:
    st.session_state['tracking_tracing7_completion_check'] = 0
if 'tracking_tracing8_completion_check' not in st.session_state:
    st.session_state['tracking_tracing8_completion_check'] = 0
if 'tracking_tracing9_completion_check' not in st.session_state:
    st.session_state['tracking_tracing9_completion_check'] = 0

if 'timeliness1_completion_check' not in st.session_state:
    st.session_state['timeliness1_completion_check'] = 0
if 'timeliness2_completion_check' not in st.session_state:
    st.session_state['timeliness2_completion_check'] = 0
if 'timeliness3_completion_check' not in st.session_state:
    st.session_state['timeliness3_completion_check'] = 0
if 'timeliness4_completion_check' not in st.session_state:
    st.session_state['timeliness4_completion_check'] = 0
if 'timeliness5_completion_check' not in st.session_state:
    st.session_state['timeliness5_completion_check'] = 0
if 'timeliness6_completion_check' not in st.session_state:
    st.session_state['timeliness6_completion_check'] = 0
if 'timeliness7_completion_check' not in st.session_state:
    st.session_state['timeliness7_completion_check'] = 0
if 'timeliness8_completion_check' not in st.session_state:
    st.session_state['timeliness8_completion_check'] = 0
if 'timeliness9_completion_check' not in st.session_state:
    st.session_state['timeliness9_completion_check'] = 0




if 'survey_completion_check' not in st.session_state:
    st.session_state['survey_completion_check'] = 'not completed'

if 'survey_sent' not in st.session_state:
    st.session_state['survey_sent'] = 'not sent'

#####################################
#define Completion Tests
#####################################
def check_completion(input_array,required_len,LPI_cat, column):
    if st.session_state['single_completion_check']== 'check completion':
        input_len=len(input_array)
        if input_len == required_len:
            st.session_state[f'{LPI_cat}{column}_completion_check']=1
            st.success('Complete')
        else:
            st.error('Add more Items')
            st.session_state[f'{LPI_cat}_completion_check']=0
            st.session_state[f'{LPI_cat}{column}_completion_check']=0
    return

def check_category_completion(LPI_cat_name):
    if st.session_state[f'{LPI_cat_name}1_completion_check'] ==1 & st.session_state[f'{LPI_cat_name}2_completion_check'] ==1 & st.session_state[f'{LPI_cat_name}3_completion_check'] ==1 & st.session_state[f'{LPI_cat_name}4_completion_check'] ==1 & st.session_state[f'{LPI_cat_name}5_completion_check'] ==1 & st.session_state[f'{LPI_cat_name}6_completion_check'] ==1& st.session_state[f'{LPI_cat_name}7_completion_check'] ==1 & st.session_state[f'{LPI_cat_name}8_completion_check'] ==1& st.session_state[f'{LPI_cat_name}9_completion_check'] ==1:
        st.success(f'{LPI_cat_name}-categorie complete')
        st.session_state[f'{LPI_cat_name}_completion_check'] = 1
    else:
        st.session_state[f'{LPI_cat_name}_completion_check'] = 0
    return



####################################
#Survey Beginn
####################################
#policy amounts to select in each Mulitselect column (Sum = 50)
pol_am_one=3
pol_am_two=4
pol_am_three=5
pol_am_four=7
pol_am_five=12

if st.session_state['language'] == 'English':
    st.subheader('1. Customs')
    st.write('**Description:** The efficiency of customs and border management clearance *(“Customs”)*. *[soucre](%s)*'%LPI_categories_Link)
    st.write('**Task:** With the goal of improving logistics in this area, please select the least appropriate policy measures first **(left)** and then proceed in order to the most appropriate measures **(right)**.')
else:
    st.subheader('1. Zoll')
    st.write('**Beschreibung:** Die Effizienz der Zoll- und Grenzabfertigung *(“Customs”)*. *[Quelle](%s)*'%LPI_categories_Link)
    st.write('**Aufgabe:** Mit dem Ziel der Verbesserung der Logistik in diesem Bereich wählen Sie bitte zuerst die am wenigsten passenden Policy-Maßnahmen **(links)** aus und fahren Sie dann der Reihe nach fort, bis hin zu den am besten passenden Maßnahmen **(rechts)**.')
 

LPI_cat='Customs'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI1 = create_column_content(pol_am_one,-4,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies1_LPI1,pol_am_one,'customs',1)
with col2:
    list_of_selected_policies2_LPI1 = create_column_content(pol_am_two,-3,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies2_LPI1,pol_am_two,'customs',2)
with col3:
    list_of_selected_policies3_LPI1 = create_column_content(pol_am_three,-2,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies3_LPI1,pol_am_three,'customs',3)
with col4:
    list_of_selected_policies4_LPI1 = create_column_content(pol_am_four,-1,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies4_LPI1,pol_am_four,'customs',4)
with col5:
    list_of_selected_policies5_LPI1 = create_column_content(pol_am_five,0,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies5_LPI1,pol_am_five,'customs',5)
with col6:
    list_of_selected_policies6_LPI1 = create_column_content(pol_am_four,1,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies6_LPI1,pol_am_four,'customs',6)
with col7:
    list_of_selected_policies7_LPI1 = create_column_content(pol_am_three,2,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies7_LPI1,pol_am_three,'customs',7)
with col8:
    list_of_selected_policies8_LPI1 = create_column_content(pol_am_two,3,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies8_LPI1,pol_am_two,'customs',8)
with col9:
    list_of_selected_policies9_LPI1 = create_column_content(pol_am_one,4,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies9_LPI1,pol_am_one,'customs',9)
check_category_completion('customs')
st.markdown('''---''')


if st.session_state['language'] == 'English':
    st.subheader('2. Infrastructure')
    st.write('**Description:** The quality of trade and transport infrastructure *(”Infrastructure”)*. *[soucre](%s)*'%LPI_categories_Link)
    st.write('**Task:** With the goal of improving logistics in this area, please select the least appropriate policy measures first **(left)** and then proceed in order to the most appropriate measures **(right)**.')
else:
    st.subheader('2. Infrastruktur')
    st.write('**Beschreibung:** Die Qualität der Handels- und Verkehrsinfrastruktur *(“Infrastructure”)*. *[Quelle](%s)*'%LPI_categories_Link)
    st.write('**Aufgabe:** Mit dem Ziel der Verbesserung der Logistik in diesem Bereich wählen Sie bitte zuerst die am wenigsten passenden Policy-Maßnahmen **(links)** aus und fahren Sie dann der Reihe nach fort, bis hin zu den am besten passenden Maßnahmen **(rechts)**.')

LPI_cat='Infrastructure'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI2 = create_column_content(pol_am_one,-4,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies1_LPI2,pol_am_one,'infrastructure',1)
with col2:
    list_of_selected_policies2_LPI2 = create_column_content(pol_am_two,-3,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies2_LPI2,pol_am_two,'infrastructure',2)
with col3:
    list_of_selected_policies3_LPI2 = create_column_content(pol_am_three,-2,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies3_LPI2,pol_am_three,'infrastructure',3)
with col4:
    list_of_selected_policies4_LPI2 = create_column_content(pol_am_four,-1,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies4_LPI2,7,'infrastructure',4)
with col5:
    list_of_selected_policies5_LPI2 = create_column_content(pol_am_five,0,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies5_LPI2,pol_am_five,'infrastructure',5)
with col6:
    list_of_selected_policies6_LPI2 = create_column_content(pol_am_four,1,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies6_LPI2,7,'infrastructure',6)
with col7:
    list_of_selected_policies7_LPI2 = create_column_content(pol_am_three,2,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies7_LPI2,pol_am_three,'infrastructure',7)
with col8:
    list_of_selected_policies8_LPI2 = create_column_content(pol_am_two,3,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies8_LPI2,pol_am_two,'infrastructure',8)
with col9:
    list_of_selected_policies9_LPI2 = create_column_content(pol_am_one,4,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies9_LPI2,pol_am_one,'infrastructure',9)  
check_category_completion('infrastructure')
st.markdown('''---''')


if st.session_state['language'] == 'English':
    st.subheader('3. Ease of arranging shipments')
    st.write('**Description:** The ease of arranging competitively priced shipments *(”Ease of arranging shipments”)*. *[soucre](%s)*'%LPI_categories_Link)
    st.write('**Task:** With the goal of improving logistics in this area, please select the least appropriate policy measures first **(left)** and then proceed in order to the most appropriate measures **(right)**.')
else:
    st.subheader('3. Preisliche Wettbewerbsfähigkeit von Sendungen')
    st.write('**Beschreibung:** Die Möglichkeit, Sendungen zu wettbewerbsfähigen Preisen zu arrangieren *("Ease of arranging shipments")*. *[Quelle](%s)*'%LPI_categories_Link)
    st.write('**Aufgabe:** Mit dem Ziel der Verbesserung der Logistik in diesem Bereich wählen Sie bitte zuerst die am wenigsten passenden Policy-Maßnahmen **(links)** aus und fahren Sie dann der Reihe nach fort, bis hin zu den am besten passenden Maßnahmen **(rechts)**.')

LPI_cat='International shipments'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI3 = create_column_content(pol_am_one,-4,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies1_LPI3,pol_am_one,'international_shipments',1)
with col2:
    list_of_selected_policies2_LPI3 = create_column_content(pol_am_two,-3,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies2_LPI3,pol_am_two,'international_shipments',2)
with col3:
    list_of_selected_policies3_LPI3 = create_column_content(pol_am_three,-2,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies3_LPI3,pol_am_three,'international_shipments',3)
with col4:
    list_of_selected_policies4_LPI3 = create_column_content(pol_am_four,-1,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies4_LPI3,pol_am_four,'international_shipments',4)
with col5:
    list_of_selected_policies5_LPI3 = create_column_content(pol_am_five,0,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies5_LPI3,pol_am_five,'international_shipments',5)
with col6:
    list_of_selected_policies6_LPI3 = create_column_content(pol_am_four,1,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies6_LPI3,pol_am_four,'international_shipments',6)
with col7:
    list_of_selected_policies7_LPI3 = create_column_content(pol_am_three,2,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies7_LPI3,pol_am_three,'international_shipments',7)
with col8:
    list_of_selected_policies8_LPI3 = create_column_content(pol_am_two,3,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies8_LPI3,pol_am_two,'international_shipments',8)
with col9:
    list_of_selected_policies9_LPI3 = create_column_content(pol_am_one,4,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies9_LPI3,pol_am_one,'international_shipments',9)
check_category_completion('international_shipments')
st.markdown('''---''')


if st.session_state['language'] == 'English':
    st.subheader('4. Quality of logistics services')
    st.write('**Description:** The competence and quality of logistics services—trucking, forwarding, and customs brokerage *(“Quality of logistics services”)*. *[soucre](%s)*'%LPI_categories_Link)
    st.write('**Task:** With the goal of improving logistics in this area, please select the least appropriate policy measures first **(left)** and then proceed in order to the most appropriate measures **(right)**.')
else:
    st.subheader('4. Qualität von Logistik Service')
    st.write('**Beschreibung:** Kompetenz und Qualität der Logistikdienstleistungen - Transport, Spedition und Zollabfertigung *("Quality of logistics services")*. *[Quelle](%s)*'%LPI_categories_Link)
    st.write('**Aufgabe:** Mit dem Ziel der Verbesserung der Logistik in diesem Bereich wählen Sie bitte zuerst die am wenigsten passenden Policy-Maßnahmen **(links)** aus und fahren Sie dann der Reihe nach fort, bis hin zu den am besten passenden Maßnahmen **(rechts)**.')


LPI_cat='Logistics competences'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI4 = create_column_content(pol_am_one,-4,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies1_LPI4,pol_am_one,'logistics_competences',1)
with col2:
    list_of_selected_policies2_LPI4 = create_column_content(pol_am_two,-3,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies2_LPI4,pol_am_two,'logistics_competences',2)
with col3:
    list_of_selected_policies3_LPI4 = create_column_content(pol_am_three,-2,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies3_LPI4,pol_am_three,'logistics_competences',3)
with col4:
    list_of_selected_policies4_LPI4 = create_column_content(pol_am_four,-1,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies4_LPI4,pol_am_four,'logistics_competences',4)
with col5:
    list_of_selected_policies5_LPI4 = create_column_content(pol_am_five,0,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies5_LPI4,pol_am_five,'logistics_competences',5)
with col6:
    list_of_selected_policies6_LPI4 = create_column_content(pol_am_four,1,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies6_LPI4,pol_am_four,'logistics_competences',6)
with col7:
    list_of_selected_policies7_LPI4 = create_column_content(pol_am_three,2,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies7_LPI4,pol_am_three,'logistics_competences',7)
with col8:
    list_of_selected_policies8_LPI4 = create_column_content(pol_am_two,3,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies8_LPI4,pol_am_two,'logistics_competences',8)
with col9:
    list_of_selected_policies9_LPI4 = create_column_content(pol_am_one,4,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies9_LPI4,pol_am_one,'logistics_competences',9)
check_category_completion('logistics_competences')
st.markdown('''---''')

if st.session_state['language'] == 'English':
    st.subheader('5. Tracking and tracing')
    st.write('**Description:** The ability to track and trace consignments *(“Tracking and tracing”)*. *[soucre](%s)*'%LPI_categories_Link)
    st.write('**Task:** With the goal of improving logistics in this area, please select the least appropriate policy measures first **(left)** and then proceed in order to the most appropriate measures **(right)**.')
else:
    st.subheader('5. Tracking und Tracing')
    st.write('**Beschreibung:** Die Möglichkeit, Sendungen zu verfolgen *("Tracking and Tracing")*. *[Quelle](%s)*'%LPI_categories_Link)
    st.write('**Aufgabe:** Mit dem Ziel der Verbesserung der Logistik in diesem Bereich wählen Sie bitte zuerst die am wenigsten passenden Policy-Maßnahmen **(links)** aus und fahren Sie dann der Reihe nach fort, bis hin zu den am besten passenden Maßnahmen **(rechts)**.')


LPI_cat='Tracking_Tracing'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI5 = create_column_content(pol_am_one,-4,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies1_LPI5,pol_am_one,'tracking_tracing',1)
with col2:
    list_of_selected_policies2_LPI5 = create_column_content(pol_am_two,-3,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies2_LPI5,pol_am_two,'tracking_tracing',2)
with col3:
    list_of_selected_policies3_LPI5 = create_column_content(pol_am_three,-2,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies3_LPI5,pol_am_three,'tracking_tracing',3)
with col4:
    list_of_selected_policies4_LPI5 = create_column_content(pol_am_four,-1,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies4_LPI5,pol_am_four,'tracking_tracing',4)
with col5:
    list_of_selected_policies5_LPI5 = create_column_content(pol_am_five,0,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies5_LPI5,pol_am_five,'tracking_tracing',5)
with col6:
    list_of_selected_policies6_LPI5 = create_column_content(pol_am_four,1,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies6_LPI5,pol_am_four,'tracking_tracing',6)
with col7:
    list_of_selected_policies7_LPI5 = create_column_content(pol_am_three,2,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies7_LPI5,pol_am_three,'tracking_tracing',7)
with col8:
    list_of_selected_policies8_LPI5 = create_column_content(pol_am_two,3,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies8_LPI5,pol_am_two,'tracking_tracing',8)
with col9:
    list_of_selected_policies9_LPI5 = create_column_content(pol_am_one,4,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies9_LPI5,pol_am_one,'tracking_tracing',9)
check_category_completion('tracking_tracing')
st.markdown('''---''')

if st.session_state['language'] == 'English':
    st.subheader('6. Timeliness')
    st.write('**Description:** The frequency with which shipments reach consignees within scheduled or expected delivery times *(“Timeliness”)*. *[soucre](%s)*'%LPI_categories_Link)
    st.write('**Task:** With the goal of improving logistics in this area, please select the least appropriate policy measures first **(left)** and then proceed in order to the most appropriate measures **(right)**.')
else:
    st.subheader('6. Pünktlichkeit')
    st.write('**Beschreibung:** Die Häufigkeit, mit der Sendungen die Empfänger innerhalb der geplanten oder erwarteten Lieferzeiten erreichen*("Timeliness")*. *[Quelle](%s)*'%LPI_categories_Link)
    st.write('**Aufgabe:** Mit dem Ziel der Verbesserung der Logistik in diesem Bereich wählen Sie bitte zuerst die am wenigsten passenden Policy-Maßnahmen **(links)** aus und fahren Sie dann der Reihe nach fort, bis hin zu den am besten passenden Maßnahmen **(rechts)**.')


LPI_cat='Timeliness'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI6 = create_column_content(pol_am_one,-4,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies1_LPI6,pol_am_one,'timeliness',1)
with col2:
    list_of_selected_policies2_LPI6 = create_column_content(pol_am_two,-3,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies2_LPI6,pol_am_two,'timeliness',2)
with col3:
    list_of_selected_policies3_LPI6 = create_column_content(pol_am_three,-2,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies3_LPI6,pol_am_three,'timeliness',3)
with col4:
    list_of_selected_policies4_LPI6 = create_column_content(pol_am_four,-1,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies4_LPI6,pol_am_four,'timeliness',4)
with col5:
    list_of_selected_policies5_LPI6 = create_column_content(pol_am_five,0,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies5_LPI6,pol_am_five,'timeliness',5)
with col6:
    list_of_selected_policies6_LPI6 = create_column_content(pol_am_four,1,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies6_LPI6,pol_am_four,'timeliness',6)
with col7:
    list_of_selected_policies7_LPI6 = create_column_content(pol_am_three,2,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies7_LPI6,pol_am_three,'timeliness',7)
with col8:
    list_of_selected_policies8_LPI6 = create_column_content(pol_am_two,3,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies8_LPI6,pol_am_two,'timeliness',8)
with col9:
    list_of_selected_policies9_LPI6 = create_column_content(pol_am_one,4,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies9_LPI6,pol_am_one,'timeliness',9)
check_category_completion('timeliness')
st.markdown('''---''')

if st.session_state['language'] == 'English':
    st.subheader('7. SAVE and SEND your entries')
    st.write('When entered the maximal amount of policies in each field continue and **SAVE** your results before **SEND**ing them in.')
    Save_Button_txt='Save your survey results'
    Info_txt='Click button again when all policies have been entered.'
    Completed_txt='Item Input complete'
else:
    st.subheader('7. SPEICHERN und ABSENDEN der Ergebnisse')
    st.write('Wenn Sie die maximale Anzahl von Richtlinien in jedes Feld eingegeben haben, fahren Sie fort und **SPEICHERN** Sie Ihre Ergebnisse, bevor Sie sie **SENDEN**.')
    Save_Button_txt='Speichern Sie Ihre Ergebnisse'
    Info_txt='Klicken Sie erneut auf den Knopf, wenn Sie alle Richtlinien eingegeben haben.'
    Completed_txt='Eingabe abgeschlossen'


save_results=st.button(Save_Button_txt)

if save_results:
    if st.session_state['single_completion_check']== 'check completion':
        st.info(Info_txt)

    if st.session_state['single_completion_check']== 'not started':
        st.session_state['single_completion_check']= 'check completion'
        st.info(Info_txt)

    if st.session_state['customs_completion_check'] == 1 & st.session_state['infrastructure_completion_check'] == 1 &st.session_state['international_shipments_completion_check'] == 1 & st.session_state['logistics_competences_completion_check'] == 1 & st.session_state['tracking_tracing_completion_check'] == 1 &st.session_state['timeliness_completion_check'] == 1:
        st.session_state['single_completion_check'] = 'completed'
        st.session_state['survey_completion_check'] = 'survey completed'     
        st.success(Completed_txt)
    






if st.session_state['survey_completion_check'] == 'survey completed' or st.session_state['survey_completion_check'] == 'survey saved' :
        df_results=pd.concat([df_results,list_of_selected_policies1_LPI1])
        df_results=pd.concat([df_results,list_of_selected_policies2_LPI1])
        df_results=pd.concat([df_results,list_of_selected_policies3_LPI1])
        df_results=pd.concat([df_results,list_of_selected_policies4_LPI1])
        df_results=pd.concat([df_results,list_of_selected_policies5_LPI1])
        df_results=pd.concat([df_results,list_of_selected_policies6_LPI1])
        df_results=pd.concat([df_results,list_of_selected_policies7_LPI1])
        df_results=pd.concat([df_results,list_of_selected_policies8_LPI1])
        df_results=pd.concat([df_results,list_of_selected_policies9_LPI1])
        df_results=pd.concat([df_results,list_of_selected_policies1_LPI2])
        df_results=pd.concat([df_results,list_of_selected_policies2_LPI2])
        df_results=pd.concat([df_results,list_of_selected_policies3_LPI2])
        df_results=pd.concat([df_results,list_of_selected_policies4_LPI2])
        df_results=pd.concat([df_results,list_of_selected_policies5_LPI2])
        df_results=pd.concat([df_results,list_of_selected_policies6_LPI2])
        df_results=pd.concat([df_results,list_of_selected_policies7_LPI2])
        df_results=pd.concat([df_results,list_of_selected_policies8_LPI2])
        df_results=pd.concat([df_results,list_of_selected_policies9_LPI2])
        df_results=pd.concat([df_results,list_of_selected_policies1_LPI3])
        df_results=pd.concat([df_results,list_of_selected_policies2_LPI3])
        df_results=pd.concat([df_results,list_of_selected_policies3_LPI3])
        df_results=pd.concat([df_results,list_of_selected_policies4_LPI3])
        df_results=pd.concat([df_results,list_of_selected_policies5_LPI3])
        df_results=pd.concat([df_results,list_of_selected_policies6_LPI3])
        df_results=pd.concat([df_results,list_of_selected_policies7_LPI3])
        df_results=pd.concat([df_results,list_of_selected_policies8_LPI3])
        df_results=pd.concat([df_results,list_of_selected_policies9_LPI3])
        df_results=pd.concat([df_results,list_of_selected_policies1_LPI4])
        df_results=pd.concat([df_results,list_of_selected_policies2_LPI4])
        df_results=pd.concat([df_results,list_of_selected_policies3_LPI4])
        df_results=pd.concat([df_results,list_of_selected_policies4_LPI4])
        df_results=pd.concat([df_results,list_of_selected_policies5_LPI4])
        df_results=pd.concat([df_results,list_of_selected_policies6_LPI4])
        df_results=pd.concat([df_results,list_of_selected_policies7_LPI4])
        df_results=pd.concat([df_results,list_of_selected_policies8_LPI4])
        df_results=pd.concat([df_results,list_of_selected_policies9_LPI4])
        df_results=pd.concat([df_results,list_of_selected_policies1_LPI5])
        df_results=pd.concat([df_results,list_of_selected_policies2_LPI5])
        df_results=pd.concat([df_results,list_of_selected_policies3_LPI5])
        df_results=pd.concat([df_results,list_of_selected_policies4_LPI5])
        df_results=pd.concat([df_results,list_of_selected_policies5_LPI5])
        df_results=pd.concat([df_results,list_of_selected_policies6_LPI5])
        df_results=pd.concat([df_results,list_of_selected_policies7_LPI5])
        df_results=pd.concat([df_results,list_of_selected_policies8_LPI5])
        df_results=pd.concat([df_results,list_of_selected_policies9_LPI5])
        df_results=pd.concat([df_results,list_of_selected_policies1_LPI6])
        df_results=pd.concat([df_results,list_of_selected_policies2_LPI6])
        df_results=pd.concat([df_results,list_of_selected_policies3_LPI6])
        df_results=pd.concat([df_results,list_of_selected_policies4_LPI6])
        df_results=pd.concat([df_results,list_of_selected_policies5_LPI6])
        df_results=pd.concat([df_results,list_of_selected_policies6_LPI6])
        df_results=pd.concat([df_results,list_of_selected_policies7_LPI6])
        df_results=pd.concat([df_results,list_of_selected_policies8_LPI6])
        df_results=pd.concat([df_results,list_of_selected_policies9_LPI6])
        df_results=pd.merge(left=df_results, right=df_policies, left_on='policies', right_on=policy_column)
        df_results=df_results[['score','LPI-categorie','Policy']]
        st.session_state['survey_completion_check'] = 'survey saved'

df_results.to_csv('data/Survey_results.csv',sep=',')

if st.session_state['language'] == 'English':
    info_saved_txt='Continue and send your results'
    Contact_txt='In case of any feedback please enter it down bellow and add your E-Mail if you would like to get sent the final analysis once it´s done.'
    Mail_Feedback_txt='Enter your E-Mail and Feedback here.'
else:
    info_saved_txt='Senden Sie nun Ihr Ergebnisse'
    Contact_txt='Falls Sie ein Feedback haben, geben Sie es bitte unten ein und fügen Sie Ihre E-Mail hinzu, wenn Sie die endgültige Analyse zugeschickt bekommen möchten, sobald sie fertig ist.'
    Mail_Feedback_txt='Geben Sie ihre E-Mail-Adresse und ihr Feedback hier ein.'

if st.session_state['survey_completion_check'] == 'survey saved':
    st.info(info_saved_txt)
    st.write(Contact_txt)
    Mail_Feedback_Input_txt=st.text_input(Mail_Feedback_txt)




########################################
#send Email
########################################

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

#app = Flask(__name__)

def send_test_mail(body):
    sender_email = "jannik.schaeffer.tu-berlin-logistik@web.de"
    receiver_email = "jannik.schaeffer.tu.berlin.log@gmail.com"

    msg = MIMEMultipart()
    msg['Subject'] = '[Q-survey Result]'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)

    with open('data/Survey_results.csv','rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name='Survey_results.csv'))

    try:
        with smtplib.SMTP('smtp.web.de', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(st.secrets['EMAIL'], st.secrets['EMAIL_PW'])
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)
        
if st.session_state['language'] == 'English':
    Send_button_txt='Click to send your survey results'
    Success_txt='Thank you for attending in this survey!'
else:
    Send_button_txt='Klicken zum Senden Sie Ihre Umfrageergebnisse'
    Success_txt='Vielen Dank für die Teilnahme an dieser Umfrage'

if st.session_state['survey_completion_check'] == 'survey saved':
    if st.button(Send_button_txt):
        body= str(Mail_Feedback_Input_txt)
        send_test_mail(body)
        st.success(Success_txt)
