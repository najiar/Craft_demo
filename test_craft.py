import unittest
import craft
from unittest import mock

FRESHDESK_TOKEN = 'kRFDaV6VTj7G3SdcYae3'

class TestCraft(unittest.TestCase):

    @mock.patch("requests.post") #fail if the link dosn't work
    def test_return_true_if_url_exists_gitHub(self, mock_post):
        mock_response = mock.Mock(status_code=200)
        mock_post.return_value = mock_response      
        craftObj = craft.Craft()
        gitData =  craftObj.getGitUser('najiar')
        self.assertEqual(gitData.status_code, 200) 

    @mock.patch("requests.post")  #fail if the link works
    def test_returns_false_if_url_exists_gitHub(self, mock_post):
        mock_response = mock.Mock(status_code=404)
        mock_post.return_value = mock_response      
        craftObj = craft.Craft()
        gitData =  craftObj.getGitUser('najiar')
        self.assertEqual(gitData.status_code, 404)
    
    @mock.patch("requests.put") #fail if the link dosn't work
    def test_return_true_if_url_exists_freshDesk_create_contact(self, mock_put):
        mock_response = mock.Mock(status_code=201)
        mock_put.return_value = mock_response
        craftObj = craft.Craft()
        freshData =  craftObj.addFreshContact('najear', FRESHDESK_TOKEN, 'Mike Anderson', '', 'Sofia', 'Developer')
        self.assertEqual(freshData.status_code, 201)
    
    @mock.patch("requests.put") #fail if the link works
    def test_return_false_if_url_exists_freshDesk_create_contact(self, mock_put):
        mock_response = mock.Mock(status_code=404)
        mock_put.return_value = mock_response
        craftObj = craft.Craft()
        freshData =  craftObj.addFreshContact('najear', FRESHDESK_TOKEN, 'Ani Petrova', '', 'Sofia', 'Developer')
        self.assertEqual(freshData.status_code, 404)
    
    
    @mock.patch("requests.post") #fail if the link dosn't work
    def test_return_true_if_url_exists_freshDesk_update_contact(self, mock_post):
        mock_response = mock.Mock(status_code=200)
        mock_post.return_value = mock_response
        craftObj = craft.Craft()
        freshData =  craftObj.updateFreshContact('najear', FRESHDESK_TOKEN, '103008026157' '', '', '', 'Web-developer')
        self.assertEqual(freshData.status_code, 200)

    
    @mock.patch("requests.post") #fail if the link works
    def test_return_false_if_url_exists_freshDesk_update_contact(self, mock_post):
        mock_response = mock.Mock(status_code=404)
        mock_post.return_value = mock_response
        craftObj = craft.Craft()
        freshData =  craftObj.updateFreshContact('najear', FRESHDESK_TOKEN, '103008026157' '', '', '', 'Web-developer')
        self.assertEqual(freshData.status_code, 404)
    

if __name__ == "__main__":
     unittest.main()