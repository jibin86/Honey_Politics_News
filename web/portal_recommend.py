import pandas as pd
import database


class portal_recommend():
    # 4개의 배열 만드는 함수
    def classify(df):
        import random
        rows = 4
        cols = 0
        classified_arr = [[0 for j in range(cols)] for i in range(rows)]

        for k in range(400):
            for cluster_index in range(4):
                if str(df['cluster'][k]) == str(cluster_index):
                    classified_arr[cluster_index].append(df['number'][k])
                elif str(df['cluster'][k]) == str(cluster_index):
                    classified_arr[cluster_index].append(df['number'][k])
                elif str(df['cluster'][k]) == str(cluster_index):
                    classified_arr[cluster_index].append(df['number'][k])
                elif str(df['cluster'][k]) == str(cluster_index):
                    classified_arr[cluster_index].append(df['number'][k])
        return classified_arr

    #4개의 배열에서 각각 9개씩 랜덤으로 뽑는 함수
    def select_portal(classified_arr):
        import random
        rows = 4
        cols = 0
        selected_index = [[0 for j in range(cols)] for i in range(rows)]

        for i in range(4):
            selected_index[i] = random.sample(classified_arr[i], 9)
        return selected_index

    #해당 기사의 추천 뉴스 4개 인덱스 반환 함수
    def news_recommend(index, classified_arr):
        import random
        for cluster_index in range(4):
            if index in classified_arr[cluster_index]:
                recommend_index = random.sample(classified_arr[cluster_index], 4)
        return recommend_index
    
    def get_rec_index(input_idx):
        idx_list = portal_recommend.news_recommend(220, portal_recommend.classify(database.df))
        data_return = database.df.iloc[idx_list]
        list_return = []
        for i in range(len(data_return)):
            list_return.append(data_return.iloc[i].tolist())
        return list_return