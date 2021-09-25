from typing import List
from django.contrib.auth import get_user_model
from django.db import models

SUB_CHOICES = [('not_set', 'not_set'), ('ACACIA RIDGE', 'ACACIA RIDGE'), ('ALBION', 'ALBION'), ('ALDERLEY', 'ALDERLEY'), ('ALGESTER', 'ALGESTER'), ('ANNERLEY', 'ANNERLEY'), ('ANSTEAD', 'ANSTEAD'), ('ARCHERFIELD', 'ARCHERFIELD'), ('ASCOT', 'ASCOT'), ('ASHGROVE', 'ASHGROVE'), ('ASPLEY', 'ASPLEY'), ('AUCHENFLOWER', 'AUCHENFLOWER'), ('BALD HILLS', 'BALD HILLS'), ('BALMORAL', 'BALMORAL'), ('BANKS CREEK', 'BANKS CREEK'), ('BANYO', 'BANYO'), ('BARDON', 'BARDON'), ('BELLBOWRIE', 'BELLBOWRIE'), ('BELMONT', 'BELMONT'), ('BOONDALL', 'BOONDALL'), ('BOWEN HILLS', 'BOWEN HILLS'), ('BRACKEN RIDGE', 'BRACKEN RIDGE'), ('BRIDGEMAN DOWNS', 'BRIDGEMAN DOWNS'), ('BRIGHTON', 'BRIGHTON'), ('BRISBANE AIRPORT', 'BRISBANE AIRPORT'), ('BRISBANE CITY', 'BRISBANE CITY'), ('BROOKFIELD', 'BROOKFIELD'), ('BULIMBA', 'BULIMBA'), ('BULWER', 'BULWER'), ('BURBANK', 'BURBANK'), ('CALAMVALE', 'CALAMVALE'), ('CAMP HILL', 'CAMP HILL'), ('CANNON HILL', 'CANNON HILL'), ('CARINA', 'CARINA'), ('CARINA HEIGHTS', 'CARINA HEIGHTS'), ('CARINDALE', 'CARINDALE'), ('CARSELDINE', 'CARSELDINE'), ('CHANDLER', 'CHANDLER'), ('CHAPEL HILL', 'CHAPEL HILL'), ('CHELMER', 'CHELMER'), ('CHERMSIDE', 'CHERMSIDE'), ('CHERMSIDE WEST', 'CHERMSIDE WEST'), ('CHUWAR', 'CHUWAR'), ('CLAYFIELD', 'CLAYFIELD'), ('COOPERS PLAINS', 'COOPERS PLAINS'), ('COORPAROO', 'COORPAROO'), ('CORINDA', 'CORINDA'), ('COWAN COWAN', 'COWAN COWAN'), ('DARRA', 'DARRA'), ('DEAGON', 'DEAGON'), ('DOOLANDELLA', 'DOOLANDELLA'), ('DREWVALE', 'DREWVALE'), ('DURACK', 'DURACK'), ('DUTTON PARK', 'DUTTON PARK'), ('EAGLE FARM', 'EAGLE FARM'), ('EAST BRISBANE', 'EAST BRISBANE'), ('EIGHT MILE PLAINS', 'EIGHT MILE PLAINS'), ('ELLEN GROVE', 'ELLEN GROVE'), ('ENGLAND CREEK', 'ENGLAND CREEK'), ('ENOGGERA', 'ENOGGERA'), ('ENOGGERA RESERVOIR', 'ENOGGERA RESERVOIR'), ('EVERTON PARK', 'EVERTON PARK'), ('FAIRFIELD', 'FAIRFIELD'), ('FERNY GROVE', 'FERNY GROVE'), ('FIG TREE POCKET', 'FIG TREE POCKET'), ('FITZGIBBON', 'FITZGIBBON'), ('FOREST LAKE', 'FOREST LAKE'), ('FORTITUDE VALLEY', 'FORTITUDE VALLEY'), ('GAYTHORNE', 'GAYTHORNE'), ('GEEBUNG', 'GEEBUNG'), ('GORDON PARK', 'GORDON PARK'), ('GRACEVILLE', 'GRACEVILLE'), ('GRANGE', 'GRANGE'), ('GREENSLOPES', 'GREENSLOPES'), ('GUMDALE', 'GUMDALE'), ('HAMILTON', 'HAMILTON'), ('HAWTHORNE', 'HAWTHORNE'), ('HEATHWOOD', 'HEATHWOOD'), ('HEMMANT', 'HEMMANT'), ('HENDRA', 'HENDRA'), ('HERSTON', 'HERSTON'), ('HIGHGATE HILL', 'HIGHGATE HILL'), ('HOLLAND PARK', 'HOLLAND PARK'), ('HOLLAND PARK WEST', 'HOLLAND PARK WEST'), ('INALA', 'INALA'), ('INDOOROOPILLY', 'INDOOROOPILLY'), ('JAMBOREE HEIGHTS', 'JAMBOREE HEIGHTS'), ('JINDALEE', 'JINDALEE'), ('KALINGA', 'KALINGA'), ('KANGAROO POINT', 'KANGAROO POINT'), ('KARANA DOWNS', 'KARANA DOWNS'), ('KARAWATHA', 'KARAWATHA'), ('KEDRON', 'KEDRON'), ('KELVIN GROVE', 'KELVIN GROVE'), ('KENMORE', 'KENMORE'), ('KENMORE HILLS', 'KENMORE HILLS'), ('KEPERRA', 'KEPERRA'), ('KHOLO', 'KHOLO'), ('KOORINGAL', 'KOORINGAL'), ('KURABY', 'KURABY'), ('LAKE MANCHESTER', 'LAKE MANCHESTER'), ('LARAPINTA', 'LARAPINTA'), ('LOTA', 'LOTA'), ('LUTWYCHE', 'LUTWYCHE'), ('LYTTON', 'LYTTON'), ('MACGREGOR', 'MACGREGOR'), ('MACKENZIE', 'MACKENZIE'), ('MANLY', 'MANLY'), ('MANLY WEST', 'MANLY WEST'), ('MANSFIELD', 'MANSFIELD'), ('MCDOWALL', 'MCDOWALL'), ('MIDDLE PARK', 'MIDDLE PARK'), ('MILTON', 'MILTON'), ('MITCHELTON', 'MITCHELTON'), ('MOGGILL', 'MOGGILL'), ('MOOROOKA', 'MOOROOKA'), ('MORETON ISLAND', 'MORETON ISLAND'), ('MORNINGSIDE', 'MORNINGSIDE'), ('MOUNT COOT-THA', 'MOUNT COOT-THA'), ('MOUNT CROSBY', 'MOUNT CROSBY'), ('MOUNT GRAVATT', 'MOUNT GRAVATT'), ('MOUNT GRAVATT EAST', 'MOUNT GRAVATT EAST'), ('MOUNT OMMANEY', 'MOUNT OMMANEY'), ('MURARRIE', 'MURARRIE'), ('NATHAN', 'NATHAN'), ('NEW FARM', 'NEW FARM'), ('NEWMARKET', 'NEWMARKET'), ('NEWSTEAD', 'NEWSTEAD'), ('NORMAN PARK', 'NORMAN PARK'), ('NORTHGATE', 'NORTHGATE'), ('NUDGEE', 'NUDGEE'), ('NUDGEE BEACH', 'NUDGEE BEACH'), ('NUNDAH', 'NUNDAH'), ('OXLEY', 'OXLEY'), ('PADDINGTON', 'PADDINGTON'), ('PALLARA', 'PALLARA'), ('PARKINSON', 'PARKINSON'), ('PETRIE TERRACE', 'PETRIE TERRACE'), ('PINJARRA HILLS', 'PINJARRA HILLS'), ('PINKENBA', 'PINKENBA'), ('PORT OF BRISBANE', 'PORT OF BRISBANE'), ('PULLENVALE', 'PULLENVALE'), ('RANSOME', 'RANSOME'), ('RED HILL', 'RED HILL'), ('RICHLANDS', 'RICHLANDS'), ('RIVERHILLS', 'RIVERHILLS'), ('ROBERTSON', 'ROBERTSON'), ('ROCHEDALE', 'ROCHEDALE'), ('ROCKLEA', 'ROCKLEA'), ('RUNCORN', 'RUNCORN'), ('SALISBURY', 'SALISBURY'), ('SANDGATE', 'SANDGATE'), ('SEVEN HILLS', 'SEVEN HILLS'), ('SEVENTEEN MILE ROCKS', 'SEVENTEEN MILE ROCKS'), ('SHERWOOD', 'SHERWOOD'), ('SHORNCLIFFE', 'SHORNCLIFFE'), ('SINNAMON PARK', 'SINNAMON PARK'), ('SOUTH BRISBANE', 'SOUTH BRISBANE'), ('SPRING HILL', 'SPRING HILL'), ('ST LUCIA', 'ST LUCIA'), ('STAFFORD', 'STAFFORD'), ('STAFFORD HEIGHTS', 'STAFFORD HEIGHTS'), ('STONES CORNER', 'STONES CORNER'), ('STRETTON', 'STRETTON'), ('SUMNER', 'SUMNER'), ('SUNNYBANK', 'SUNNYBANK'), ('SUNNYBANK HILLS', 'SUNNYBANK HILLS'), ('TAIGUM', 'TAIGUM'), ('TARINGA', 'TARINGA'), ('TARRAGINDI', 'TARRAGINDI'), ('TENERIFFE', 'TENERIFFE'), ('TENNYSON', 'TENNYSON'), ('THE GAP', 'THE GAP'), ('TINGALPA', 'TINGALPA'), ('TOOWONG', 'TOOWONG'), ('UPPER BROOKFIELD', 'UPPER BROOKFIELD'), ('UPPER KEDRON', 'UPPER KEDRON'), ('UPPER MOUNT GRAVATT', 'UPPER MOUNT GRAVATT'), ('VIRGINIA', 'VIRGINIA'), ('WACOL', 'WACOL'), ('WAKERLEY', 'WAKERLEY'), ('WAVELL HEIGHTS', 'WAVELL HEIGHTS'), ('WEST END', 'WEST END'), ('WESTLAKE', 'WESTLAKE'), ('WILLAWONG', 'WILLAWONG'), ('WILSTON', 'WILSTON'), ('WINDSOR', 'WINDSOR'), ('WISHART', 'WISHART'), ('WOOLLOONGABBA', 'WOOLLOONGABBA'), ('WOOLOOWIN', 'WOOLOOWIN'), ('WYNNUM', 'WYNNUM'), ('WYNNUM WEST', 'WYNNUM WEST'), ('YEERONGPILLY', 'YEERONGPILLY'), ('YERONGA', 'YERONGA'), ('ZILLMERE', 'ZILLMERE')]

# PROJECT
class Project(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, #if i delete the user, delete their projects too
        related_name='owner_projects'
    )
    title = models.CharField(max_length=200)
    suburbs = models.CharField(
        max_length=100,
        choices=SUB_CHOICES,
        default='not_set',
    )
    description = models.TextField()
    beehives = models.IntegerField(null=True)
    image = models.URLField()
    date_created = models.DateTimeField()
    min_required = models.IntegerField(default=300) 
    is_open = models.BooleanField()

    @property
    def goal(self):
        return self.beehives * 300

    # @property
    # def status(self):
    #     # all_related_pledges = self.pledge_set.objects.all()
    #     all_related_pledges = Pledge.objects.filter(project=self.id)
    #     total_pledge_amount = 0
    #     for pledge in all_related_pledges:
    #         total_pledge_amount += pledge.amount
    #     # total_amount = sum(pledge.amount for pledge in all_related_pledges)
    #     return round(total_pledge_amount/(self.beehives * 300), 2)

    @property
    def status(self):
        all_related_pledges = Pledge.objects.filter(project=self.id)
        total_pledge_amount = 0
        current_status = 0
        for pledge in all_related_pledges:
            total_pledge_amount += pledge.amount
            current_status = round(total_pledge_amount/(self.beehives * 300), 2)
        if current_status >= 1:
            return "closed"
        return current_status

    @property
    def show_all_categorys(self):
        all_categories = self.category_set.all()
        category_names = []
        for category in all_categories:
            category_names.append(category.category)
        return category_names


# CATEGORY
class Category(models.Model):
    category = models.CharField(max_length=200)
    projects = models.ManyToManyField(Project)


# PLEDGE
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
        )
    #point supporter to the user
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

   
    
# BEEFRIEND
class Beefriend(models.Model):
    comment = models.CharField(max_length=200)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='beefriend'
        )
    beefriend = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='befriender'
    )