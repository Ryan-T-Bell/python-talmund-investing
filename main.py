import yfinance as yf

GBTC_DATE = '2017-01-02'

def merge_dfs(df0, df1):
        df = df0.merge(df1, on='Date')  
        df['Ratio'] = df['Close_x'] / df['Close_y']
        return calculate_moving_averages(df)

def calculate_moving_averages(df):
        df['50'] = df['Ratio'].rolling(window=50).mean()
        df['200'] = df['Ratio'].rolling(window=200).mean()
        return df

def get_ma_score(df):
        if str(df['50'].tail(1).values >= df['200'].tail(1).values) == '[ True]':
                return 1
        return 0

def main():
        # Base Calculation
        moat = yf.Ticker('VUG').history(start=GBTC_DATE)
        xlre = yf.Ticker('XLRE').history(start=GBTC_DATE)
        gnr = yf.Ticker('GNR').history(start=GBTC_DATE)
        btc = yf.Ticker('BTC-USD').history(start=GBTC_DATE)
        gld = yf.Ticker('GLD').history(start=GBTC_DATE)
        tlt = yf.Ticker('TLT').history(start=GBTC_DATE)

        # Price in MOAT (Stocks)
        moat_moat = merge_dfs(moat, moat)
        xlre_moat = merge_dfs(xlre, moat)
        gnr_moat = merge_dfs(gnr, moat)
        gbtc_moat = merge_dfs(btc, moat)
        gld_moat = merge_dfs(gld, moat)

        # Price in XLRE (Real Estate)
        moat_xlre = merge_dfs(moat, xlre)
        xlre_xlre = merge_dfs(xlre, xlre)
        gnr_xlre = merge_dfs(gnr, xlre)
        gbtc_xlre = merge_dfs(btc, xlre)
        gld_xlre = merge_dfs(gld, xlre)
  
        # Price in GNR (Commodities)
        moat_gnr = merge_dfs(moat, gnr)
        xlre_gnr = merge_dfs(xlre, gnr)
        gnr_gnr = merge_dfs(gnr, gnr)
        gbtc_gnr = merge_dfs(btc, gnr)
        gld_gnr = merge_dfs(gld, gnr)

        # Price in BTC (Bitcoin)
        moat_gbtc = merge_dfs(moat, btc)
        xlre_gbtc = merge_dfs(xlre, btc)
        gnr_gbtc = merge_dfs(gnr, btc)
        gbtc_gbtc = merge_dfs(btc, btc)
        gld_gbtc = merge_dfs(gld, btc)

        # Price in GLD (Gold)
        moat_gld = merge_dfs(moat, gld)
        xlre_gld = merge_dfs(xlre, gld)
        gnr_gld = merge_dfs(gnr, gld)
        gbtc_gld = merge_dfs(btc, gld)

        # Price in Treasuries (TLT)
        moat_tlt = merge_dfs(moat, tlt)
        xlre_tlt = merge_dfs(xlre, tlt)
        gnr_tlt = merge_dfs(gnr, tlt)
        gld_tlt = merge_dfs(gld, tlt)
        gbtc_tlt = merge_dfs(btc, tlt)
        tlt_tlt = merge_dfs(tlt, tlt)

        # Calculate Rankings
        rank_moat = get_ma_score(moat_xlre) + get_ma_score(moat_gnr) + get_ma_score(moat_gbtc) + get_ma_score(moat_gld)
        rank_xlre = get_ma_score(xlre_moat) + get_ma_score(xlre_gnr) + get_ma_score(xlre_gbtc) + get_ma_score(xlre_gld)
        rank_grn = get_ma_score(gnr_moat) + get_ma_score(gnr_xlre) + get_ma_score(gnr_gbtc) + get_ma_score(gnr_gld)
        rank_btc = get_ma_score(gbtc_moat) + get_ma_score(gbtc_xlre) + get_ma_score(gbtc_gnr) + get_ma_score(gbtc_gld)
        rank_gld = get_ma_score(gld_moat) + get_ma_score(gld_xlre) + get_ma_score(gld_gnr) + get_ma_score(gld_gbtc)
        
        print('SCORES\n=======================\nHigher = Most momentum\nLower = Recent bearish\n=======================')
        print('Stock (VUG) = ' + str(rank_moat))
        print('Real Estate (XLRE) = ' + str(rank_xlre))
        print('Commodities (GRN) = ' + str( rank_grn))
        print('Bitcoin (BTC-USD) = ' + str(rank_btc))
        print('Gold (GLD) = ' + str(rank_gld))


if __name__ == "__main__":
        main()
