bact_plas_dict = {}
bact_plas_list = '''FlavobacteriaceaeFlavobacterialesFlavo-bacteria1 PE, PET, PP, North Sea, Baltic Sea,
PS
reference
33,35–37,39,55–57
Mediterranean Sea, North
Atlantic Ocean, Humber
Estuary, North Pacific
Ocean
Saprospiraceae
Sphingobacteriales
Sphingo-
PE, PET, ND Yangtze Estuary, North
bacteria1
31,35,39,40,58
Atlantic Ocean, North
Pacific Ocean, Baltic Sea
Hyphomonadaceae
Rhodobacterales
Alpha-
PE, PP, PS
proteobacteria2
North Sea, North Atlantic 31,33,37,39,40,59
Ocean, Baltic Sea,
Mediterranean Sea, North
Pacific Ocean
Rhodobacteraceae
Rhodobacterales
Alpha-PE, PET, PP, Baltic Sea, Mediterranean 31,33,35,37,39,55,57–
proteobacteria2PS, ND
Sea, North Atlantic
60
Ocean, North Pacific
Ocean, North Sea,
Yangtze Estuary
Erythrobacteraceae
Sphingomonadales
Alpha-
PE, PP, ND
proteobacteria2
North Sea, Mediterranean, Sea, North Atlantic
Ocean, Yangtze Estuary,
Baltic Sea
Sphingomonadaceae
Sphingomonadales
Alpha-PE, PP, PS,North Atlantic Ocean,
proteobacteria2NDYangtze Estuary, Baltic
37,40,58,59
Sea
Comamonadaceae
Burkholderiales
Beta-
PET, PS, ND Baltic Sea, North Atlantic 37,40,58,59
proteobacteria2
Alcanivoracaceae
Oceanospirillales
Gamma-
Ocean, Yangtze Estuary
PE, PET, PS North Sea, Mediterranean 35,56
proteobacteria2
Pseudoaltero-monadaceae Alteromonadales
Oceanospirillaceae
Oceanospirillales
Sea
Gamma-PE, PP, PS,North Sea, North Atlantic 31,38,55,58
proteobacteria2NDOcean, Yangtze Estuary
Gamma-PE, PET, PS North Atlantic Ocean,
proteobacteria2
31,35,56,57
Mediterranean Sea, North
Sea
Vibrionaceae
Vibrionales
Gamma-
proteobacteria2
78
1
PE, PP, PS
North Sea, North Atlantic 31,38,55
Ocean'''.split()

for i in bact_plas_list:
    if i not in bact_plas_dict:
        bact_plas_dict[i] = 1
    else:
        bact_plas_dict[i] = 1 +bact_plas_dict[i]

bact_plas_dict = {k: v for k, v in sorted(bact_plas_dict.items(), key=lambda item: item[1],reverse = True)}

print(bact_plas_dict)
