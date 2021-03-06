# pylint: disable=no-self-use # pyATS-related exclusion
from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.browsers import Chrome
from oct.pages.review import Review, Rating
from oct.pages.product_page import ProductPage
from oct.tests import run_testcase


class UsersReview(Testcase):
    @test
    def test(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        product_page = ProductPage(chrome, "33", "Samsung SyncMaster 941BW")
        product_page.load(device)
        product_page.open_review_link()
        review_tab = Review(chrome)
        review_tab.type_name("AutoTestBot")
        review_tab.type_review("This review has been wrote by auto test bot!")
        review_tab.choose_rating(Rating.THREE)
        review_tab.press_continue()
        assert review_tab.successfully_added()


if __name__ == "__main__":
    run_testcase()
