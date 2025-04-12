from datetime import datetime, timedelta
import pandas as pd
import jdatetime    
import io

def get_new_fun_pos(funners, io_data):
    

    df = pd.read_excel(io_data, engine='openpyxl')

    break_point_day = datetime.now() - timedelta(days=30)
    white_list = {}

    for column_name, column_data in df.items():
        column_name = str(column_name).strip()
        if column_name.startswith('Unnamed') or column_name == 'Date' or column_name.startswith('#'):
            continue
        
        tmp_date = df['Date'][0]
        ls_use_funners = []
        
        for index, raw_value in enumerate(column_data):
            
            if isinstance(raw_value, float) and str(raw_value) != 'nan':
                value = int(raw_value)
            else:
                value = raw_value

            if isinstance(df['Date'][index], datetime):
                tmp_date = df['Date'][index]

            m_str = tmp_date.strftime('%m') 
            d_str = tmp_date.strftime('%d')
            
            if m_str == '01':
                x= '1404'
            else: 
                x='1403'

            date_obj = jdatetime.datetime.strptime(f'{x}-{m_str}-{d_str}', '%Y-%m-%d')

            gregorian_date = date_obj.togregorian()

            print(break_point_day, gregorian_date , f'{x}-{m_str}-{d_str}', break_point_day < gregorian_date)
            if break_point_day < gregorian_date  :
                
                if str(value) != 'nan' and str(value) in funners:
                    ls_use_funners.append(str(value))

        not_used_funners = set(funners) - set(ls_use_funners)
        
        real_funners = {int(i.replace('+', '').replace('-', '')) : i for i in list(not_used_funners) if i.endswith('+') or i.startswith('-')}
        sorted_real_funners = list(real_funners.keys())
        sorted_real_funners.sort()
        real_funners = [real_funners[i] for i in sorted_real_funners]

        shared_funners = {int(i.replace('*', '')) : i for i in list(not_used_funners) if i.startswith('*')}
        sorted_shared_funners = list(shared_funners.keys())
        sorted_shared_funners.sort()
        shared_funners = [shared_funners[i] for i in sorted_shared_funners]


        just_me = list(int(i) for i in (not_used_funners - (set(real_funners + shared_funners) )))
        just_me.sort()
        white_list[column_name] = real_funners + just_me + shared_funners

    
    try:
        new_df = pd.DataFrame(white_list)
    
    except ValueError:
        # Normalize the dictionary if the lengths are inconsistent
        max_length = max(len(v) for v in white_list.values())
        normalized_data = {
            key: value + [None] * (max_length - len(value))
            for key, value in white_list.items()
        }
        new_df = pd.DataFrame(normalized_data)

    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        new_df.to_excel(writer, index=False)
    
    
    buffer.seek(0)

    return buffer.getvalue()
