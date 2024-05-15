from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

class ExpandingCards(BaseCase):
  def test_expanding_cards(self):
    self.open('http://127.0.0.1:5500/expanding_cards/index.html')

    self.assert_element('div.panel:nth-child(1).active')

    self.click('div.panel:nth-child(2)')
    self.assert_element_not_present('div.panel:nth-child(1).active')
    self.assert_element('div.panel:nth-child(2).active')

    self.click('div.panel:nth-child(3)')
    self.assert_element_not_present('div.panel:nth-child(2).active')
    self.assert_element('div.panel:nth-child(3).active')

    self.click('div.panel:nth-child(4)')
    self.assert_element_not_present('div.panel:nth-child(3).active')
    self.assert_element('div.panel:nth-child(4).active')

    self.click('div.panel:nth-child(5)')
    self.assert_element_not_present('div.panel:nth-child(4).active')
    self.assert_element('div.panel:nth-child(5).active')