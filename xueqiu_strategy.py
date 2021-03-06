from xueqiu_api import XueqiuApi


class XueqiuStrategies(object):
    @staticmethod
    def stable_strict():
        stable = XueqiuApi('stable_strict')
        stable.append_pettm('0', '15')
        stable.append_pb()
        stable.append_dy()
        stable.append_roediluted('20160930', '10', is_order_by_this=True)
        stable.append_roediluted('20151231', '15')
        stable.append_roediluted('20141231', '15')
        stable.append_roediluted('20131231', '15')
        stable.append_roediluted('20121231', '15')
        stable.append_roediluted('20111231', '12')
        stable.append_roediluted('20101231', '10')
        stable.append_roediluted('20091231', '10')

        stable.append_income_grow('20160930')
        stable.append_income_grow('20151231')
        stable.append_income_grow('20141231')
        stable.append_income_grow('20131231')
        stable.append_income_grow('20121231')
        stable.append_income_grow('20111231')
        stable.append_income_grow('20101231')
        stable.append_income_grow('20091231')

        stable.append_profie_grow('20160930')
        stable.append_profie_grow('20151231')
        stable.append_profie_grow('20141231')
        stable.append_profie_grow('20131231')
        stable.append_profie_grow('20121231')
        stable.append_profie_grow('20111231')
        stable.append_profie_grow('20101231')
        stable.append_profie_grow('20091231')

        stable.append_gross('20160930')
        stable.append_gross('20151231')
        stable.append_gross('20141231')
        stable.append_gross('20131231')
        stable.append_gross('20121231')
        # stable.append_gross('20111231')
        # stable.append_gross('20101231')
        # stable.append_gross('20091231')

        stable.append_interest('20160930')
        stable.append_interest('20151231')
        stable.append_interest('20141231')
        stable.append_interest('20131231')
        stable.append_interest('20121231')
        # stable.append_interest('20111231')
        # stable.append_interest('20101231')
        # stable.append_interest('20091231')
        return stable

    @staticmethod
    def stable_short():
        stable = XueqiuApi('stable_short')
        stable.append_pettm('0', '30')
        stable.append_pb()
        stable.append_dy()
        stable.append_roediluted('20160930', '10', is_order_by_this=True)
        stable.append_roediluted('20151231', '15')
        stable.append_roediluted('20141231', '15')
        stable.append_roediluted('20131231', '15')
        stable.append_roediluted('20121231', '15')

        stable.append_income_grow('20160930')
        stable.append_income_grow('20151231')
        stable.append_income_grow('20141231')
        stable.append_income_grow('20131231')
        stable.append_income_grow('20121231')

        stable.append_profie_grow('20160930')
        stable.append_profie_grow('20151231')
        stable.append_profie_grow('20141231')
        stable.append_profie_grow('20131231')
        stable.append_profie_grow('20121231')

        stable.append_gross('20160930')
        stable.append_gross('20151231')
        stable.append_gross('20141231')
        stable.append_gross('20131231')
        stable.append_gross('20121231')

        stable.append_interest('20160930')
        stable.append_interest('20151231')
        stable.append_interest('20141231')
        stable.append_interest('20131231')
        stable.append_interest('20121231')
        return stable

    @staticmethod
    def stable():
        stable = XueqiuApi('stable')
        stable.append_pettm('0', '25')
        stable.append_pb()
        stable.append_dy()
        stable.append_roediluted('20160930', '10', is_order_by_this=True)
        stable.append_roediluted('20151231', '15')
        stable.append_roediluted('20141231', '15')
        stable.append_roediluted('20131231', '15')
        stable.append_roediluted('20121231', '15')
        stable.append_roediluted('20111231', '12')
        stable.append_roediluted('20101231', '10')
        stable.append_roediluted('20091231', '10')

        stable.append_income_grow('20160930')
        stable.append_income_grow('20151231')
        stable.append_income_grow('20141231')
        stable.append_income_grow('20131231')
        stable.append_income_grow('20121231')
        stable.append_income_grow('20111231')
        stable.append_income_grow('20101231')
        stable.append_income_grow('20091231')

        stable.append_profie_grow('20160930')
        stable.append_profie_grow('20151231')
        stable.append_profie_grow('20141231')
        stable.append_profie_grow('20131231')
        stable.append_profie_grow('20121231')
        stable.append_profie_grow('20111231')
        stable.append_profie_grow('20101231')
        stable.append_profie_grow('20091231')

        stable.append_gross('20160930')
        stable.append_gross('20151231')
        stable.append_gross('20141231')
        stable.append_gross('20131231')
        stable.append_gross('20121231')
        # stable.append_gross('20111231')
        # stable.append_gross('20101231')
        # stable.append_gross('20091231')

        stable.append_interest('20160930')
        stable.append_interest('20151231')
        stable.append_interest('20141231')
        stable.append_interest('20131231')
        stable.append_interest('20121231')
        # stable.append_interest('20111231')
        # stable.append_interest('20101231')
        # stable.append_interest('20091231')
        return stable

    @staticmethod
    def stable_slow():
        stable = XueqiuApi('stable_slow')
        stable.append_pettm('0', '25')
        stable.append_pb()
        stable.append_dy()
        stable.append_roediluted('20160930', '10', is_order_by_this=True)
        stable.append_roediluted('20151231', '15')
        stable.append_roediluted('20141231', '15')
        stable.append_roediluted('20131231', '15')
        stable.append_roediluted('20121231', '12')
        stable.append_roediluted('20111231', '10')
        stable.append_roediluted('20101231', '10')
        stable.append_roediluted('20091231', '8')

        stable.append_income_grow('20160930')
        stable.append_income_grow('20151231')
        stable.append_income_grow('20141231')
        stable.append_income_grow('20131231')
        stable.append_income_grow('20121231')
        stable.append_income_grow('20111231')
        stable.append_income_grow('20101231')
        stable.append_income_grow('20091231')

        stable.append_profie_grow('20160930')
        stable.append_profie_grow('20151231')
        stable.append_profie_grow('20141231')
        stable.append_profie_grow('20131231')
        stable.append_profie_grow('20121231')
        stable.append_profie_grow('20111231')
        stable.append_profie_grow('20101231')
        stable.append_profie_grow('20091231')

        stable.append_gross('20160930')
        stable.append_gross('20151231')
        stable.append_gross('20141231')
        stable.append_gross('20131231')
        stable.append_gross('20121231')
        # stable.append_gross('20111231')
        # stable.append_gross('20101231')
        # stable.append_gross('20091231')

        stable.append_interest('20160930')
        stable.append_interest('20151231')
        stable.append_interest('20141231')
        stable.append_interest('20131231')
        stable.append_interest('20121231')
        # stable.append_interest('20111231')
        # stable.append_interest('20101231')
        # stable.append_interest('20091231')
        return stable

    @staticmethod
    def faster_short():
        fast = XueqiuApi('faster_short')
        fast.append_pettm('0', '30')
        fast.append_pb()
        fast.append_dy()
        fast.append_roediluted('20160930', '10', is_order_by_this=True)
        fast.append_roediluted('20151231', '20')
        fast.append_roediluted('20141231', '10')
        fast.append_roediluted('20131231')
        fast.append_roediluted('20121231')

        fast.append_income_grow('20160930', '7')
        fast.append_income_grow('20151231', '7')
        fast.append_income_grow('20141231', '7')
        fast.append_income_grow('20131231')
        fast.append_income_grow('20121231')

        fast.append_profie_grow('20160930', '10')
        fast.append_profie_grow('20151231', '12')
        fast.append_profie_grow('20141231', '12')
        fast.append_profie_grow('20131231')
        fast.append_profie_grow('20121231')

        fast.append_gross('20160930')
        fast.append_gross('20151231')
        fast.append_gross('20141231')
        fast.append_gross('20131231')
        fast.append_gross('20121231')

        fast.append_interest('20160930')
        fast.append_interest('20151231')
        fast.append_interest('20141231')
        fast.append_interest('20131231')
        fast.append_interest('20121231')
        return fast

    @staticmethod
    def fast():
        fast = XueqiuApi('fast')
        fast.append_pettm('0', '30')
        fast.append_pb()
        fast.append_dy()
        fast.append_roediluted('20160930', '10')
        fast.append_roediluted('20151231', '20', is_order_by_this=True)
        fast.append_roediluted('20141231', '15')
        fast.append_roediluted('20131231')
        fast.append_roediluted('20121231')
        fast.append_roediluted('20111231')
        fast.append_roediluted('20101231')
        fast.append_roediluted('20091231')

        fast.append_income_grow('20160930', '5')
        fast.append_income_grow('20151231', '5')
        fast.append_income_grow('20141231', '5')
        fast.append_income_grow('20131231')
        fast.append_income_grow('20121231')
        fast.append_income_grow('20111231')
        fast.append_income_grow('20101231')
        fast.append_income_grow('20091231')

        fast.append_profie_grow('20160930', '7')
        fast.append_profie_grow('20151231', '10')
        fast.append_profie_grow('20141231', '10')
        fast.append_profie_grow('20131231')
        fast.append_profie_grow('20121231')
        fast.append_profie_grow('20111231')
        fast.append_profie_grow('20101231')
        fast.append_profie_grow('20091231')

        fast.append_gross('20160930')
        fast.append_gross('20151231')
        fast.append_gross('20141231')
        fast.append_gross('20131231')
        fast.append_gross('20121231')
        # fast.append_gross('20111231')
        # fast.append_gross('20101231')
        # fast.append_gross('20091231')

        fast.append_interest('20160930')
        fast.append_interest('20151231')
        fast.append_interest('20141231')
        fast.append_interest('20131231')
        fast.append_interest('20121231')
        # fast.append_interest('20111231')
        # fast.append_interest('20101231')
        # fast.append_interest('20091231')
        return fast

    @staticmethod
    def faster():
        fast = XueqiuApi('faster')
        fast.append_pettm('0', '30')
        fast.append_pb()
        fast.append_dy()
        fast.append_roediluted('20160930', '10', is_order_by_this=True)
        fast.append_roediluted('20151231', '20')
        fast.append_roediluted('20141231', '10')
        fast.append_roediluted('20131231')
        fast.append_roediluted('20121231')
        fast.append_roediluted('20111231')
        fast.append_roediluted('20101231')
        fast.append_roediluted('20091231')

        fast.append_income_grow('20160930', '7')
        fast.append_income_grow('20151231', '7')
        fast.append_income_grow('20141231', '7')
        fast.append_income_grow('20131231')
        fast.append_income_grow('20121231')
        fast.append_income_grow('20111231')
        fast.append_income_grow('20101231')
        fast.append_income_grow('20091231')

        fast.append_profie_grow('20160930', '10')
        fast.append_profie_grow('20151231', '12')
        fast.append_profie_grow('20141231', '12')
        fast.append_profie_grow('20131231')
        fast.append_profie_grow('20121231')
        fast.append_profie_grow('20111231')
        fast.append_profie_grow('20101231')
        fast.append_profie_grow('20091231')

        fast.append_gross('20160930')
        fast.append_gross('20151231')
        fast.append_gross('20141231')
        fast.append_gross('20131231')
        fast.append_gross('20121231')
        # fast.append_gross('20111231')
        # fast.append_gross('20101231')
        # fast.append_gross('20091231')

        fast.append_interest('20160930')
        fast.append_interest('20151231')
        fast.append_interest('20141231')
        fast.append_interest('20131231')
        fast.append_interest('20121231')
        # fast.append_interest('20111231')
        # fast.append_interest('20101231')
        # fast.append_interest('20091231')
        return fast

    @staticmethod
    def fastest():
        fast = XueqiuApi('fastest')
        fast.append_pettm('0', '35')
        fast.append_pb()
        fast.append_dy()
        fast.append_roediluted('20160930', '12', is_order_by_this=True)
        fast.append_roediluted('20151231', '20')
        fast.append_roediluted('20141231', '10')
        fast.append_roediluted('20131231')
        fast.append_roediluted('20121231')
        fast.append_roediluted('20111231')
        fast.append_roediluted('20101231')
        fast.append_roediluted('20091231')

        fast.append_income_grow('20160930', '10')
        fast.append_income_grow('20151231', '10')
        fast.append_income_grow('20141231', '10')
        fast.append_income_grow('20131231')
        fast.append_income_grow('20121231')
        fast.append_income_grow('20111231')
        fast.append_income_grow('20101231')
        fast.append_income_grow('20091231')

        fast.append_profie_grow('20160930', '15')
        fast.append_profie_grow('20151231', '18')
        fast.append_profie_grow('20141231', '18')
        fast.append_profie_grow('20131231')
        fast.append_profie_grow('20121231')
        fast.append_profie_grow('20111231')
        fast.append_profie_grow('20101231')
        fast.append_profie_grow('20091231')

        fast.append_gross('20160930')
        fast.append_gross('20151231')
        fast.append_gross('20141231')
        fast.append_gross('20131231')
        fast.append_gross('20121231')
        # fast.append_gross('20111231')
        # fast.append_gross('20101231')
        # fast.append_gross('20091231')

        fast.append_interest('20160930')
        fast.append_interest('20151231')
        fast.append_interest('20141231')
        fast.append_interest('20131231')
        fast.append_interest('20121231')
        # fast.append_interest('20111231')
        # fast.append_interest('20101231')
        # fast.append_interest('20091231')
        return fast
