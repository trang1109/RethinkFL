import os
import pandas as pd
import numpy as np
from argparse import ArgumentParser

path = './data/'
scenarios_list = ['fl_digits', 'fl_officecaltech']
structures_list = ['homogeneity', 'heterogeneity']  # Adding heterogeneity for example
pri_aug = 'weak'  # weak, strong
column_mean_acc_list = ['method', 'paragroup'] + ['epoch' + str(i) for i in range(40)] + ['MEAN']
domain_list = ['intra', 'inter']

def load_mean_acc_list(structure_path, domain):
    acc_dict = {}
    experiment_index = 0
    for model in os.listdir(structure_path):
        if model != '':
            model_path = os.path.join(structure_path, model)
            if os.path.isdir(model_path):
                for para in os.listdir(model_path):
                    para_path = os.path.join(model_path, para)
                    args_path = para_path + '/args.csv'
                    args_pd = pd.read_table(args_path, sep=",")
                    args_pd = args_pd.loc[:, args_pd.columns]
                    args_pri_aug = args_pd['pri_aug'][0]
                    if args_pri_aug == pri_aug:
                        if len(os.listdir(para_path)) != 1:
                            data = pd.read_table(para_path + '/mean_' + domain + '.csv', sep=",")
                            data = data.loc[:, data.columns]
                            acc_value = data.values
                            mean_acc_value = np.mean(acc_value, axis=0)
                            mean_acc_value = mean_acc_value.tolist()
                            mean_acc_value = [round(item, 2) for item in mean_acc_value]
                            last_acc_value = mean_acc_value[-3:]
                            last_acc_value = np.mean(last_acc_value)
                            mean_acc_value.append(round(last_acc_value, 3))
                            acc_dict[experiment_index] = [model, para] + mean_acc_value
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
        for _, structure in enumerate(structures_list):
            for _, domain in enumerate(domain_list):
                print(f'Scenario: {scenario} Structure: {structure} Domain: {domain} Augmentation: {pri_aug}')
                structure_path = os.path.join(scenario_path, structure)
                mean_acc_dict = load_mean_acc_list(structure_path, domain)
                mean_df = pd.DataFrame(mean_acc_dict)
                mean_df = mean_df.T
                mean_df.columns = column_mean_acc_list
                print(mean_df)
                mean_df.to_excel(os.path.join(structure_path, domain + '_output.xls'), na_rep=True)

if __name__ == '__main__':
    main()
