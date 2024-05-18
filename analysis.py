import os
import pandas as pd
import numpy as np
from argparse import ArgumentParser

path = './data/'
scenarios_list = ['fl_digits', 'fl_officecaltech']
pri_aug = 'weak'  # weak, strong
column_mean_acc_list = ['method', 'paragroup', 'MEAN']
domain_list = ['inter']

def load_mean_acc_list(scenario_path, domain):
    acc_dict = {}
    experiment_index = 0
    for model in os.listdir(scenario_path):
        if model != '':
            model_path = os.path.join(scenario_path, model)
            if os.path.isdir(model_path):
                for para in os.listdir(model_path):
                    para_path = os.path.join(model_path, para)
                    args_path = para_path + '/args.csv'
                    args_pd = pd.read_table(args_path, sep=",")
                    args_pri_aug = args_pd['pri_aug'][0]
                    if args_pri_aug == pri_aug:
                        data_filename = 'mean_acc.csv'
                        data_path = os.path.join(para_path, data_filename)
                        if os.path.exists(data_path):
                            data = pd.read_table(data_path, sep=",")
                            acc_value = data.values
                            mean_acc_value = np.mean(acc_value, axis=0)  # Mean of each column
                            overall_mean = np.mean(mean_acc_value)  # Overall mean of all means
                            acc_dict[experiment_index] = [model, para, round(overall_mean, 3)]
                            experiment_index += 1
    return acc_dict

def parse_args():
    parser = ArgumentParser(description='Analysis Configuration')
    parser.add_argument('--pri_aug', type=str, default='weak', choices=['weak', 'strong'])
    return parser.parse_args()

def main():
    args = parse_args()
    global pri_aug
    pri_aug = args.pri_aug

    for _, scenario in enumerate(scenarios_list):
        print('**************************************************************')
        scenario_path = os.path.join(path, scenario)
        for _, domain in enumerate(domain_list):
            print(f'Scenario: {scenario} Domain: {domain} Augmentation: {pri_aug}')
            mean_acc_dict = load_mean_acc_list(scenario_path, domain)
            mean_df = pd.DataFrame.from_dict(mean_acc_dict, orient='index', columns=column_mean_acc_list)
            print(mean_df)
            output_file_name = f"{scenario}_{domain}_output.xlsx"
            output_file_path = os.path.join(scenario_path, output_file_name)
            mean_df.to_excel(output_file_path, na_rep='True')

if __name__ == '__main__':
    main()
