best_args = {
    'fl_digits': {
        'feddf': {
            -1: {
                'communication_epoch': 40,
                'local_lr': 0.001,
                'public_lr': 0.001,
                'local_epoch': 20,
                'public_epoch': 1,
                'public_batch_size': 256,
                'local_batch_size': 128,
            },
        },
        'fccl': {
            -1: {
                'communication_epoch': 40,
                'local_lr': 0.001,
                'public_lr': 0.001,
                'local_epoch': 20,
                'public_epoch': 1,
                'public_batch_size': 256,
                'local_batch_size': 128,
                'off_diag_weight': 0.0051,

            },
        },
        'fcclplus': {
            -1: {
                'communication_epoch': 40,
                'local_lr': 0.001,
                'public_lr': 0.001,
                'local_epoch': 20,
                'public_epoch': 1,
                'public_batch_size': 256,
                'local_batch_size': 128,
                'temp': 0.02,
                'dis_power': 3,
                'local_dis_power': 3
            },
        },
        'fedavg': {
                'local_lr': 0.01,
                'local_batch_size': 64,
        },
        'fedprox': {
                'local_lr': 0.01,
                'local_batch_size': 64,
                'mu': 0.01,
        },

        'moon': {
                'local_lr': 0.01,
                'local_batch_size': 64,
                'temperature': 0.5,
                'mu':5
        },

        'fpl': {
            'local_lr': 0.01,
            'local_batch_size': 64,
            'Note': '+ MSE'
        }
    },
    'fl_officecaltech': {
        'feddf': {
            -1: {
                'communication_epoch': 40,
                'local_lr': 0.001,
                'public_lr': 0.001,
                'local_epoch': 20,
                'public_epoch': 1,
                'public_batch_size': 256,
                'local_batch_size': 128,
            },
        },
        'fccl': {
            -1: {
                'communication_epoch': 40,
                'local_lr': 0.001,
                'public_lr': 0.001,
                'local_epoch': 20,
                'public_epoch': 1,
                'public_batch_size': 256,
                'local_batch_size': 128,
                'off_diag_weight': 0.0051,

            },
        },
        'fcclplus': {
            -1: {
                'communication_epoch': 40,
                'local_lr': 0.001,
                'public_lr': 0.001,
                'local_epoch': 20,
                'public_epoch': 1,
                'public_batch_size': 256,
                'local_batch_size': 128,
                'temp': 0.02,
                'dis_power': 3,
                'local_dis_power': 3
            },
        },
        'fedavg': {
            'local_lr': 0.01,
            'local_batch_size': 64,
        },
        'fedprox': {
            'local_lr': 0.01,
            'mu': 0.01,
            'local_batch_size': 64,
        },
        'moon': {
            'local_lr': 0.01,
            'local_batch_size': 64,
            'temperature': 0.5,
            'mu': 5
        },

        'fpl': {
            'local_lr': 0.01,
            'local_batch_size': 64,
            'Note': '+ MSE'
        }
    },
    

    
}
