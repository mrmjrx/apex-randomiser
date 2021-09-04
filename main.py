import pandas as pd

MAX_RANK_DIFFERENCE = 0
MAX_DPS_DIFFERENCE = 50

weapons_df = pd.read_csv("data/weapons.csv")


def get_loadouts(num_of_loadouts=2):
    loadouts = []
    loadouts_valid = False

    while not loadouts_valid:
        loadouts = []
        for i in range(0, num_of_loadouts):
            loadout_is_valid = False
            loadout = []
            while not loadout_is_valid:
                sample = weapons_df.sample(n=2)
                loadout = [sample.iloc[0].squeeze(), sample.iloc[1].squeeze()]

                loadout_is_valid = loadout[0].weapon != loadout[1].weapon  # Only requirement for now - more done later
            loadouts.append(loadout)
            del loadout

        total_dps = [n[0].dps + n[1].dps for n in loadouts]
        rank_total = [n[0].rank_num + n[1].rank_num for n in loadouts]

        if num_of_loadouts > 1:
            dps_diff = max(total_dps) - min(total_dps)
            rank_diff = max(rank_total) - min(rank_total)

            if rank_diff <= MAX_RANK_DIFFERENCE and dps_diff <= MAX_DPS_DIFFERENCE:
                loadouts_valid = True

                if total_dps[0] < total_dps[1]:
                    loadout = loadouts.pop()
                    loadouts.insert(0, loadout)
        else:
            loadouts_valid = True
    return loadouts


if __name__ == '__main__':
    print(get_loadouts())
