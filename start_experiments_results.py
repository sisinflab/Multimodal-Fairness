from elliot.run import run_experiment

config = """experiment:
  backend: pytorch
  data_config:
    strategy: fixed
    train_path: ../data/{0}/train.txt
    validation_path: ../data/{0}/val.txt
    test_path: ../data/{0}/test.txt
  dataset: dataset_name
  top_k: 50
  evaluation:
    cutoffs: [10, 20, 50]
    simple_metrics: [nDCG, Recall, Precision, HR, MAR, MAP, MRR, F1, ACLT, APLT, ARP, PopREO, PopRESP, ItemCoverage, Gini, SE]
    complex_metrics:
      - metric: BiasDisparityBD
        user_clustering_name: WarmColdUsers
        user_clustering_file: ../data/dataset_name/user_groups_pareto.tsv
        item_clustering_name: WarmColdItem
        item_clustering_file: ../data/dataset_name/item_groups_pareto.tsv
      - metric: BiasDisparityBR
        user_clustering_name: WarmColdUsers
        user_clustering_file: ../data/dataset_name/user_groups_pareto.tsv
        item_clustering_name: WarmColdItem
        item_clustering_file: ../data/dataset_name/item_groups_pareto.tsv
      - metric: BiasDisparityBS
        user_clustering_name: WarmColdUsers
        user_clustering_file: ../data/dataset_name/user_groups_pareto.tsv
        item_clustering_name: WarmColdItem
        item_clustering_file: ../data/dataset_name/item_groups_pareto.tsv
      - metric: UserMADranking
        clustering_name: WarmColdUsers
        clustering_file: ../data/dataset_name/user_groups_pareto.tsv
      - metric: UserMADrating
        clustering_name: WarmColdUsers
        clustering_file: ../data/dataset_name/user_groups_pareto.tsv
      - metric: ItemMADranking
        clustering_name: WarmColdItems
        clustering_file: ../data/dataset_name/item_groups_pareto.tsv
      - metric: ItemMADrating
        clustering_name: WarmColdItems
        clustering_file: ../data/dataset_name/item_groups_pareto.tsv
      - metric: REO
        clustering_name: WarmColdItems
        clustering_file: ../data/dataset_name/item_groups_pareto.tsv
      - metric: RSP
        clustering_name: WarmColdItems
        clustering_file: ../data/dataset_name/item_groups_pareto.tsv
      - metric: clustered_nDCG
        user_clustering_name: WarmColdUsers
        user_clustering_file: ../data/dataset_name/user_groups_pareto.tsv
      - metric: clustered_GiniIndex
        user_clustering_name: WarmColdUsers
        user_clustering_file: ../data/dataset_name/user_groups_pareto.tsv
      - metric: clustered_Recall
        user_clustering_name: WarmColdUsers
        user_clustering_file: ../data/dataset_name/user_groups_pareto.tsv
      - metric: clustered_APLT
        user_clustering_name: WarmColdUsers
        user_clustering_file: ../data/dataset_name/user_groups_pareto.tsv
  gpu: -1
  external_models_path: ../external/models/__init__.py
  models:
    RecommendationFolder:
      folder: ./results/dataset_name/recs/
"""

datasets = ['beauty', 'clothing', 'sports', 'toys', 'office']

for d in datasets:
    with open(f'./config_files/{d}_results.yml', 'w') as f:
        f.write(config.replace('dataset_name', d))
    run_experiment(f"config_files/{d}_results.yml")
