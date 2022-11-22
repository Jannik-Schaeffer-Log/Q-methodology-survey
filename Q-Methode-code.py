########################################
# Import libraries
########################################
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Q-Methodology", page_icon="🥑",layout="wide")

########################################
# Read Data
########################################
df_policies= pd.read_csv('https://github.com/Jannik-Schaeffer-Log/Q-methodology-survey/blob/main/data/Policies.csv', delimiter=';')

all_policies=df_policies['Policy Component '].unique()

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
st.header('Q-Methodology')
st.write('Please sort the policies from most to least fitting ones in regard to the particular LPI-factor.')

with st.expander('Click to see all available policies') :
    st.dataframe(all_policies)
    

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
st.subheader('1. Customs')
st.write('Description of LPI-Faktor: Customs')
LPI_cat='Customs'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI1 = create_column_content(4,-4,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies1_LPI1,4,'customs',1)
with col2:
    list_of_selected_policies2_LPI1 = create_column_content(5,-3,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies2_LPI1,5,'customs',2)
with col3:
    list_of_selected_policies3_LPI1 = create_column_content(6,-2,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies3_LPI1,6,'customs',3)
with col4:
    list_of_selected_policies4_LPI1 = create_column_content(7,-1,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies4_LPI1,7,'customs',4)
with col5:
    list_of_selected_policies5_LPI1 = create_column_content(8,0,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies5_LPI1,8,'customs',5)
with col6:
    list_of_selected_policies6_LPI1 = create_column_content(7,1,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies6_LPI1,7,'customs',6)
with col7:
    list_of_selected_policies7_LPI1 = create_column_content(6,2,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies7_LPI1,6,'customs',7)
with col8:
    list_of_selected_policies8_LPI1 = create_column_content(5,3,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies8_LPI1,5,'customs',8)
with col9:
    list_of_selected_policies9_LPI1 = create_column_content(4,4,policies_LPI1)
    policies_LPI1=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI1['policies']), policies_LPI1))
    check_completion(list_of_selected_policies9_LPI1,4,'customs',9)
check_category_completion('customs')

st.subheader('2. Infrastructure')
st.write('Description of LPI-Faktor: Infrastructure')
LPI_cat='Infrastructure'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI2 = create_column_content(4,-4,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies1_LPI2,4,'infrastructure',1)
with col2:
    list_of_selected_policies2_LPI2 = create_column_content(5,-3,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies2_LPI2,5,'infrastructure',2)
with col3:
    list_of_selected_policies3_LPI2 = create_column_content(6,-2,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies3_LPI2,6,'infrastructure',3)
with col4:
    list_of_selected_policies4_LPI2 = create_column_content(7,-1,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies4_LPI2,7,'infrastructure',4)
with col5:
    list_of_selected_policies5_LPI2 = create_column_content(8,0,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies5_LPI2,8,'infrastructure',5)
with col6:
    list_of_selected_policies6_LPI2 = create_column_content(7,1,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies6_LPI2,7,'infrastructure',6)
with col7:
    list_of_selected_policies7_LPI2 = create_column_content(6,2,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies7_LPI2,6,'infrastructure',7)
with col8:
    list_of_selected_policies8_LPI2 = create_column_content(5,3,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies8_LPI2,5,'infrastructure',8)
with col9:
    list_of_selected_policies9_LPI2 = create_column_content(4,4,policies_LPI2)
    policies_LPI2=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI2['policies']), policies_LPI2))
    check_completion(list_of_selected_policies9_LPI2,4,'infrastructure',9)  
check_category_completion('infrastructure')

st.subheader('3. International shipments')
st.write('Description of LPI-Faktor: International shipments')
LPI_cat='International shipments'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI3 = create_column_content(4,-4,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies1_LPI3,4,'international_shipments',1)
with col2:
    list_of_selected_policies2_LPI3 = create_column_content(5,-3,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies2_LPI3,5,'international_shipments',2)
with col3:
    list_of_selected_policies3_LPI3 = create_column_content(6,-2,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies3_LPI3,6,'international_shipments',3)
with col4:
    list_of_selected_policies4_LPI3 = create_column_content(7,-1,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies4_LPI3,7,'international_shipments',4)
with col5:
    list_of_selected_policies5_LPI3 = create_column_content(8,0,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies5_LPI3,8,'international_shipments',5)
with col6:
    list_of_selected_policies6_LPI3 = create_column_content(7,1,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies6_LPI3,7,'international_shipments',6)
with col7:
    list_of_selected_policies7_LPI3 = create_column_content(6,2,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies7_LPI3,6,'international_shipments',7)
with col8:
    list_of_selected_policies8_LPI3 = create_column_content(5,3,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies8_LPI3,5,'international_shipments',8)
with col9:
    list_of_selected_policies9_LPI3 = create_column_content(4,4,policies_LPI3)
    policies_LPI3=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI3['policies']), policies_LPI3))
    check_completion(list_of_selected_policies9_LPI3,4,'international_shipments',9)
check_category_completion('international_shipments')

st.subheader('4. Logistics competences')
st.write('Description of LPI-Faktor: Logistics competences')
LPI_cat='Logistics competences'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI4 = create_column_content(4,-4,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies1_LPI4,4,'logistics_competences',1)
with col2:
    list_of_selected_policies2_LPI4 = create_column_content(5,-3,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies2_LPI4,5,'logistics_competences',2)
with col3:
    list_of_selected_policies3_LPI4 = create_column_content(6,-2,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies3_LPI4,6,'logistics_competences',3)
with col4:
    list_of_selected_policies4_LPI4 = create_column_content(7,-1,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies4_LPI4,7,'logistics_competences',4)
with col5:
    list_of_selected_policies5_LPI4 = create_column_content(8,0,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies5_LPI4,8,'logistics_competences',5)
with col6:
    list_of_selected_policies6_LPI4 = create_column_content(7,1,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies6_LPI4,7,'logistics_competences',6)
with col7:
    list_of_selected_policies7_LPI4 = create_column_content(6,2,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies7_LPI4,6,'logistics_competences',7)
with col8:
    list_of_selected_policies8_LPI4 = create_column_content(5,3,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies8_LPI4,5,'logistics_competences',8)
with col9:
    list_of_selected_policies9_LPI4 = create_column_content(4,4,policies_LPI4)
    policies_LPI4=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI4['policies']), policies_LPI4))
    check_completion(list_of_selected_policies9_LPI4,4,'logistics_competences',9)
check_category_completion('logistics_competences')

st.subheader('5. Tracking & tracing')
st.write('Description of LPI-Faktor: Tracking & tracing')
LPI_cat='Tracking_Tracing'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI5 = create_column_content(4,-4,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies1_LPI5,4,'tracking_tracing',1)
with col2:
    list_of_selected_policies2_LPI5 = create_column_content(5,-3,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies2_LPI5,5,'tracking_tracing',2)
with col3:
    list_of_selected_policies3_LPI5 = create_column_content(6,-2,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies3_LPI5,6,'tracking_tracing',3)
with col4:
    list_of_selected_policies4_LPI5 = create_column_content(7,-1,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies4_LPI5,7,'tracking_tracing',4)
with col5:
    list_of_selected_policies5_LPI5 = create_column_content(8,0,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies5_LPI5,8,'tracking_tracing',5)
with col6:
    list_of_selected_policies6_LPI5 = create_column_content(7,1,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies6_LPI5,7,'tracking_tracing',6)
with col7:
    list_of_selected_policies7_LPI5 = create_column_content(6,2,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies7_LPI5,6,'tracking_tracing',7)
with col8:
    list_of_selected_policies8_LPI5 = create_column_content(5,3,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies8_LPI5,5,'tracking_tracing',8)
with col9:
    list_of_selected_policies9_LPI5 = create_column_content(4,4,policies_LPI5)
    policies_LPI5=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI5['policies']), policies_LPI5))
    check_completion(list_of_selected_policies9_LPI5,4,'tracking_tracing',9)
check_category_completion('tracking_tracing')

st.subheader('6. Timeliness')
st.write('Description of LPI-Faktor: Timeliness')
LPI_cat='Timeliness'
col1, col2, col3, col4, col5, col6, col7, col8, col9, = st.columns(9)
with col1:
    list_of_selected_policies1_LPI6 = create_column_content(4,-4,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies1_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies1_LPI6,4,'timeliness',1)
with col2:
    list_of_selected_policies2_LPI6 = create_column_content(5,-3,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies2_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies2_LPI6,5,'timeliness',2)
with col3:
    list_of_selected_policies3_LPI6 = create_column_content(6,-2,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies3_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies3_LPI6,6,'timeliness',3)
with col4:
    list_of_selected_policies4_LPI6 = create_column_content(7,-1,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies4_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies4_LPI6,7,'timeliness',4)
with col5:
    list_of_selected_policies5_LPI6 = create_column_content(8,0,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies5_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies5_LPI6,8,'timeliness',5)
with col6:
    list_of_selected_policies6_LPI6 = create_column_content(7,1,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies6_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies6_LPI6,7,'timeliness',6)
with col7:
    list_of_selected_policies7_LPI6 = create_column_content(6,2,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies7_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies7_LPI6,6,'timeliness',7)
with col8:
    list_of_selected_policies8_LPI6 = create_column_content(5,3,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies8_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies8_LPI6,5,'timeliness',8)
with col9:
    list_of_selected_policies9_LPI6 = create_column_content(4,4,policies_LPI6)
    policies_LPI6=list(filter(lambda x: x not in list(list_of_selected_policies9_LPI6['policies']), policies_LPI6))
    check_completion(list_of_selected_policies9_LPI6,4,'timeliness',9)
check_category_completion('timeliness')

save_results=st.button('Save your survey results')
if save_results:
    if st.session_state['single_completion_check']== 'not started':
        st.session_state['single_completion_check']= 'check completion'
        st.info('Click button again when completed')
    
    if st.session_state['customs_completion_check'] == 1 & st.session_state['infrastructure_completion_check'] == 1 &st.session_state['international_shipments_completion_check'] == 1 & st.session_state['logistics_competences_completion_check'] == 1 & st.session_state['tracking_tracing_completion_check'] == 1 &st.session_state['timeliness_completion_check'] == 1:
        st.session_state['survey_completion_check'] = 'survey completed'     
        st.success('Item Input complete')





if st.session_state['survey_completion_check'] == 'survey completed':
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

st.write('Results')
st.dataframe(df_results)
df_results.to_csv('data/Survey_results.csv',sep=',')






########################################
#send Email
########################################


# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# from email.mime.text import MIMEText
# import smtplib

# def send_mail():
#     # Create a multipart message
#     msg = MIMEMultipart()
#     body_part = MIMEText('Test', 'plain')
#     msg['Subject'] = 'Test Mail'
#     msg['From'] = 'jannik.schaeffer.tu.berlin.log@gmail.com'
#     msg['To'] = 'jannik.schaeffer.tu.berlin.log@gmail.com'
#     # Add body to email
#     msg.attach(body_part)
#     # open and read the CSV file in binary
#     # with open('data\Survey_results.csv','rb') as file:
#     # # Attach the file with filename to the email
#     #     msg.attach(MIMEApplication(file.read(), Name='Survey_results.csv'))
#     # Create SMTP object
#     smtp_obj = smtplib.SMTP('smtp.gmail.com', 465)
#     # Login to the server
#     smtp_obj.login('jannik.schaeffer.tu.berlin.log@gmail.com','Logistik4TUBerlin')
#     # Convert the message to a string and send it
#     smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
#     smtp_obj.quit()

# if st.button('Send your survey results'):
#     send_mail()

from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

app = Flask(__name__)

def send_test_mail(body):
    sender_email = "jannik.schaeffer.tu-berlin-logistik@web.de"
    receiver_email = "jannik.schaeffer.tu.berlin.log@gmail.com"

    msg = MIMEMultipart()
    msg['Subject'] = '[Email Test]'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)

    with open('data\Survey_results.csv','rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name='Survey_results.csv'))

    try:
        with smtplib.SMTP('smtp.web.de', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("jannik.schaeffer.tu-berlin-logistik@web.de", "Logistik4TUBerlin")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)
        
# @app.route('/')
# def hello_world():
#     return "Hello world!"


if st.button('Send your survey results'):
    send_test_mail('Q-Methode Results')
    st.success('Thank you for attending in this survey!')
