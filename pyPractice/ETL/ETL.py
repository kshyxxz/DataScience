import pandas as pd
import logging, time, schedule
import os

current_dir = os.path.dirname(__file__)   
base_dir = os.path.dirname(current_dir)  
file_path = os.path.join(base_dir, 'datasets', 'data.csv')

df = pd.read_csv(file_path)

logging.basicConfig(
	filename=os.path.join(base_dir, 'ETL.log'),
	level=logging.INFO,
	format='%(asctime)s - %(levelname)s - %(message)s'
)

def pipeline():
	logging.info('ETL pipeline started')
	try: 
		df = pd.read_csv(file_path)
		logging.info('Data loaded successfully')
		df['age'] = df['age'].fillna(df['age'].mean())
		logging.info('Data cleaned successfully')
		df.to_csv(os.path.join(base_dir, 'datasets', 'cleaned_data.csv'), index=False)
		logging.info('Data saved successfully')
	except Exception as e:
		logging.error(f'Error in ETL pipeline: {e}')

schedule.every(5).seconds.do(pipeline)

if __name__ == "__main__":
	while True:
		schedule.run_pending()
		time.sleep(1)