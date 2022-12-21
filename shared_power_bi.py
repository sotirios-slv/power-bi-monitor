import json
import requests
import pandas as pd

from shared_azure import authenticate_by_client_token

access_token = authenticate_by_client_token()

def get_data_from_power_bi(endpoint):

    base_url = 'https://api.powerbi.com/v1.0/myorg/'
    header = {'Authorization': f'Bearer {access_token}'}

    request = requests.get(f'{base_url}{endpoint}', headers=header)
    content = json.loads(request.content)

    return content

def get_refresh_history():

    refresh_history = {}

    groups = get_data_from_power_bi('groups')
    groups = groups.get('value')
    if not groups:
        print('No groups returned')
        return
    
    for group in groups:
        
        group_id = group['id']
        group_name = group['name']

        refresh_history[group_name] = {}

        datasets = get_data_from_power_bi(f'admin/groups/{group_id}/datasets')
        datasets = datasets.get('value')
        
        if not datasets:
            print(f'No datasets retrieved for {group_name}')
        
        for dataset in datasets:

            dataset_id = dataset['id']
            dataset_name = dataset['name']
            dataset_refresh_history = get_data_from_power_bi(f'groups/{group_id}/datasets/{dataset_id}/refreshes')

            dataset_refresh_history = dataset_refresh_history.get('value')
            
            refresh_history[group_name][dataset_name] = dataset_refresh_history
    
    return refresh_history

def get_dataset_summary_df():

    columns = ['workspace', 'workspace_id', 'dataset', 'dataset_id', 'isRefreshable','refresh_id','refreshType','startTime','endTime','refreshStatus']
    data=[]

    groups = get_data_from_power_bi('groups')
    groups = groups.get('value')

    if not groups:
        print('No groups returned')
        return
    for group in groups:
        group_id = group['id']
        group_name = group['name']

        datasets = get_data_from_power_bi(f'admin/groups/{group_id}/datasets')
        datasets = datasets.get('value')

        if not datasets:
            data.append([group_name, group_id,'','','','','','','',''])
            print(f'No datasets retrieved for {group_name}')

        for dataset in datasets:
            dataset_id = dataset['id']
            dataset_refresh_history = get_data_from_power_bi(f'groups/{group_id}/datasets/{dataset_id}/refreshes')
            dataset_refresh_history = dataset_refresh_history.get('value')
            
            if not dataset_refresh_history:
                data.append([group_name, group_id,dataset['name'],dataset_id,dataset['isRefreshable'],'','','','',''])
                print('No refresh history')
            else:
                for refresh in dataset_refresh_history[:3]:
                    data.append([group_name, group_id,dataset['name'],dataset_id,dataset['isRefreshable'],refresh['id'],refresh['refreshType'],refresh['startTime'],refresh['endTime'],refresh['status']])

    df = pd.DataFrame(data=data, columns=columns)

    return df

get_dataset_summary_df()