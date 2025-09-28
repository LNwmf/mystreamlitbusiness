from sheets import submit_business_to_sheet

#submit_business_to_sheet(
#    business_name="Test from CLI",
#    description="Testing direct submit",
#    website="https://example.com",
#    image_url="https://example.com/logo.png",
#    category="Retail",
#    email="testemail.com",
#)
submit_business_to_sheet(
    "Test Business",
    "A description",
    "https://testwebsite.com",
    "https://imageurl.com/image.jpg",
    "Test Category",
    "test@example.com"
)
