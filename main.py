import yfinance as yf
from chart import ChartView

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
        moat = yf.Ticker('MOAT').history(start=GBTC_DATE)
        xlre = yf.Ticker('XLRE').history(start=GBTC_DATE)
        vcmdx = yf.Ticker('VCMDX').history(start=GBTC_DATE)
        gbtc = yf.Ticker('GBTC').history(start=GBTC_DATE)
        gld = yf.Ticker('GLD').history(start=GBTC_DATE)

        # Price in MOAT (Stocks)
        moat_moat = merge_dfs(moat, moat)
        xlre_moat = merge_dfs(xlre, moat)
        vcmdx_moat = merge_dfs(vcmdx, moat)
        gbtc_moat = merge_dfs(gbtc, moat)
        gld_moat = merge_dfs(gld, moat)
        # ChartView('MOAT', moat_moat, xlre_moat, vcmdx_moat, gbtc_moat, gld_moat)

        # Price in XLRE (Real Estate)
        moat_xlre = merge_dfs(moat, xlre)
        xlre_xlre = merge_dfs(xlre, xlre)
        vcmdx_xlre = merge_dfs(vcmdx, xlre)
        gbtc_xlre = merge_dfs(gbtc, xlre)
        gld_xlre = merge_dfs(gld, xlre)
        # ChartView('XLRE', moat_xlre, xlre_xlre, vcmdx_xlre, gbtc_xlre, gld_xlre)

        # Price in VCMDX (Commodities)
        moat_vcmdx = merge_dfs(moat, vcmdx)
        xlre_vcmdx = merge_dfs(xlre, vcmdx)
        vcmdx_vcmdx = merge_dfs(vcmdx, vcmdx)
        gbtc_vcmdx = merge_dfs(gbtc, vcmdx)
        gld_vcmdx = merge_dfs(gld, vcmdx)
        # ChartView('VCMDX', moat_vcmdx, xlre_vcmdx, vcmdx_vcmdx, gbtc_vcmdx, gld_vcmdx)

        # Price in GBTC (Bitcoin)
        moat_gbtc = merge_dfs(moat, gbtc)
        xlre_gbtc = merge_dfs(xlre, gbtc)
        vcmdx_gbtc = merge_dfs(vcmdx, gbtc)
        gbtc_gbtc = merge_dfs(gbtc, gbtc)
        gld_gbtc = merge_dfs(gld, gbtc)
        # ChartView('GBTC', moat_gbtc, xlre_gbtc, vcmdx_gbtc, gbtc_gbtc, gld_gbtc)
        
        # Price in GLD (Gold)
        moat_gld = merge_dfs(moat, gld)
        xlre_gld = merge_dfs(xlre, gld)
        vcmdx_gld = merge_dfs(vcmdx, gld)
        gbtc_gld = merge_dfs(gbtc, gld)
        gld_gld = merge_dfs(gld, gld)
        # ChartView('GLD', moat_gld, xlre_gld, vcmdx_gld, gbtc_gld, gld_gld)

        print('MOAT = ' +
        str(
                get_ma_score(moat_xlre) + 
                get_ma_score(moat_vcmdx) + 
                get_ma_score(moat_gbtc) + 
                get_ma_score(moat_gld)
                )
        )

        print('XLRE = ' +
        str(
                get_ma_score(xlre_moat) + 
                get_ma_score(xlre_vcmdx) + 
                get_ma_score(xlre_gbtc) + 
                get_ma_score(xlre_gld)
                )
        )

        print('VCMDX = ' +
        str( 
                get_ma_score(vcmdx_moat) + 
                get_ma_score(vcmdx_xlre) + 
                get_ma_score(vcmdx_gbtc) + 
                get_ma_score(vcmdx_gld)
                )
        )

        print('GBTC = ' +
        str(
                get_ma_score(gbtc_moat) + 
                get_ma_score(gbtc_xlre) + 
                get_ma_score(gbtc_vcmdx) +  
                get_ma_score(gbtc_gld)
                )
        )

        print('GLD = ' +
        str(
                get_ma_score(gld_moat) + 
                get_ma_score(gld_xlre) + 
                get_ma_score(gld_vcmdx) + 
                get_ma_score(gld_gbtc)
                )
        )


if __name__ == "__main__":
        main()
