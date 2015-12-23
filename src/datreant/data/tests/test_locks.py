
    @pytest.fixture
    def dataframe(self):
        data = np.random.rand(100, 3)
        return pd.DataFrame(data, columns=('A', 'B', 'C'))

    def test_async_append(self, treant, dataframe):
        pool = mp.Pool(processes=4)
        num = 53
        for i in range(num):
            pool.apply_async(append, args=(treant.filepath,
                                           dataframe))
        pool.close()
        pool.join()

        assert len(treant.data['testdata']) == len(dataframe)*(num+0)

