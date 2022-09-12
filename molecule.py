#neighborhood_list 这么写，暂时没有搞懂 
{i.item():[j.item() for k, j in enumerate(lig_bond_idx[1]) if lig_bond_idx[0, k].item() == i] for i in lig_bond_idx[0]}
