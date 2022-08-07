import matplotlib.pyplot as plt
from matplotlib.image import imread
from tempfile import NamedTemporaryFile
import yfinance as yf

GBTC_DATE = '2017-01-02'

class ChartView:

    def __init__(self, symbol, moat, xlre, vcmdx, gbtc, gld):
        self.symbol = symbol
        self.add_data_to_graph(moat, xlre, vcmdx, gbtc, gld)
        self.show_chart()

    def add_data_to_graph(self, moat, xlre, vcmdx, gbtc, gld):
        moat['Ratio'].plot(color = 'green', kind='line')
        xlre['Ratio'].plot(color = 'red', kind='line')
        vcmdx['Ratio'].plot(color = 'brown', kind='line')
        gbtc['Ratio'].plot(color = 'orange', kind='line')
        gld['Ratio'].plot(color = 'yellow', kind='line')


    def show_chart(self):
        fig = plt.figure(1)
        title = yf.Ticker(self.symbol).info['longName'] + ' (' + self.symbol + ')'
        plt.title(title, fontsize=20)

        plt.xlabel('Date')
        plt.ylabel('Price Ratio')

        plt.rc('font', size=11)
        plt.legend(loc=2)

        plt.show()

# HELPER METHODS OUTSIDE VIEW -----------------------------------------------------------------


def get_size(fig, dpi=100):
    with NamedTemporaryFile(suffix='.png') as f:
        fig.savefig(f.name, bbox_inches='tight', dpi=dpi)
        height, width, _channels = imread(f.name).shape
        return width / dpi, height / dpi


def set_size(fig, size, dpi=100, eps=1e-2, give_up=2, min_size_px=10):
    target_width, target_height = size
    set_width, set_height = target_width, target_height  # reasonable starting point
    deltas = []  # how far we have
    while True:
        fig.set_size_inches([set_width, set_height])
        actual_width, actual_height = get_size(fig, dpi=dpi)
        set_width *= target_width / actual_width
        set_height *= target_height / actual_height
        deltas.append(abs(actual_width - target_width) + abs(actual_height - target_height))
        if deltas[-1] < eps:
            return True
        if len(deltas) > give_up and sorted(deltas[-give_up:]) == deltas[-give_up:]:
            return False
        if set_width * dpi < min_size_px or set_height * dpi < min_size_px:
            return False


def main():
    symbols_list = ['MOAT', 'XLRE', 'GBTC', 'GLD']
    for symbol in symbols_list:
        ChartView(symbol, '', True)


if __name__ == '__main__':
    main()

