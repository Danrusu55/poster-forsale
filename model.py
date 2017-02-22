# -*- coding: utf-8 -*-
import sys
# Get input
# campaign = input('Enter campaign: ')

# regular
#campaign = sys.argv[1]
#print(campaign)

'''
if campaign == 'plumbing':
    citiesArray = [
        #['https://austin.craigslist.org','512-402-3182'],
        ['https://sanantonio.craigslist.org','210-598-5062'],
        ['https://houston.craigslist.org/','281-408-4220'],
        ['https://dallas.craigslist.org','214-463-2122'],
        ['https://newjersey.craigslist.org/','732-391-4474'],
        ['https://nyc.craigslist.org/','718-395-6399'],
        ['https://baltimore.craigslist.org/','410-695-8169'],
        ['https://norfolk.craigslist.org/','757-690-2042'],
        ['https://raleigh.craigslist.org/','916-943-4133'],
        ['https://charlotte.craigslist.org/','704-837-0972'],
        ['https://columbia.craigslist.org/','803-489-8740'],
        ['https://atlanta.craigslist.org/','404-962-8582'],
        ['https://tampa.craigslist.org/','813-413-5110'],
        ['https://miami.craigslist.org/','786-431-0130'],
        ['https://orlando.craigslist.org/','407-395-4610'],
        ['https://jacksonville.craigslist.org/','904-342-1278'],
        ['https://akroncanton.craigslist.org/','330-935-9041'],
        ['https://cleveland.craigslist.org/','440-379-1356'],
        ['https://detroit.craigslist.org/','313-263-5162'],
        ['https://minneapolis.craigslist.org/','651-504-0801'],
        ['https://chicago.craigslist.org/','312-234-0357'],
        ['https://stlouis.craigslist.org/','314-403-1911'],
        ['https://kansascity.craigslist.org/','816-326-1032'],
        ['https://seattle.craigslist.org/','206-981-3196'],
        ['https://phoenix.craigslist.org/','503-946-5213'],
        ['https://honolulu.craigslist.org/','808-518-2788'],
        ['https://sacramento.craigslist.org/','916-347-9370'],
        ['https://inlandempire.craigslist.org/','909-219-9430'],
        ['https://orangecounty.craigslist.org/','949-284-4845'],
        ['https://losangeles.craigslist.org/','303-536-8775'],
        ['https://sandiego.craigslist.org/','605-777-0112'],
        ['https://phoenix.craigslist.org/','602-884-8503'],
        ['https://denver.craigslist.org','303-625-9351'],
        ['https://elpaso.craigslist.org/','915-209-4257'],
        ['https://cosprings.craigslist.org/','719-569-8577'],
    ]
elif campaign == 'roofing':
    citiesArray = [
        #['http://inlandempire.craigslist.org/','951-999-4026'],
        #['http://orangecounty.craigslist.org','949-415-5014'],
        #['http://portland.craigslist.org/','503-549-1177'],
        #['http://seattle.craigslist.org','206-429-8264'],
        #['http://sfbay.craigslist.org/','415-683-1810'],
        #['https://akroncanton.craigslist.org/','330-791-3224'],
        #['https://austin.craigslist.org','512-456-9665'],
        #['https://baltimore.craigslist.org/','443-602-9295'],
        #['https://boise.craigslist.org/','208-957-5710'],
        #['https://charlotte.craigslist.org/','704-761-6010'],
        #['https://chicago.craigslist.org','312-234-0375'],
        #['https://cleveland.craigslist.org/','440-202-1401'],
        #['https://cnj.craigslist.org/','732-943-1815'],
        #['https://columbia.craigslist.org/','803-792-0342'],
        #['https://columbus.craigslist.org/','614-524-4205'],
        #['https://cosprings.craigslist.org/','719-299-3073'],
        #['https://dallas.craigslist.org','214-494-8155'],
        #['https://denver.craigslist.org','720-924-4640'],
        #['https://detroit.craigslist.org','313-915-4226'],
        #['https://hartford.craigslist.org/','860-288-5660'],
        #['https://houston.craigslist.org/','281-661-7076'],
        #['https://jacksonville.craigslist.org/','904-770-3001'],
        #['https://longisland.craigslist.org/','718-514-7945'],
        #['https://losangeles.craigslist.org/','323-621-3799'],
        #['https://miami.craigslist.org/','786-319-9133'],
        #['https://minneapolis.craigslist.org','612-999-1507'],
        #['https://norfolk.craigslist.org/','757-818-9211'],
        #['https://nyc.craigslist.org/','718-618-5869'],
        #['https://orlando.craigslist.org/','407-502-4930'],
        #['https://philadelphia.craigslist.org/','610-981-1670'],
        #['https://pittsburgh.craigslist.org/','612-999-2276'],
        #['https://raleigh.craigslist.org/','919-351-1401'],
        #['https://richmond.craigslist.org/','804-491-3560'],
        #['https://sanantonio.craigslist.org','210-598-5027'],
        #['https://stlouis.craigslist.org','314-403-7301'],
        #['https://tampa.craigslist.org/','813-602-7311']
    ]
elif campaign == 'electrical':
    citiesArray = [
        ['https://atlanta.craigslist.org/','678-899-6530'],
        ['https://baltimore.craigslist.org/','443-637-1520'],
        ['https://chicago.craigslist.org/','312-647-2114'],
        ['https://cincinnati.craigslist.org/','513-259-2071'],
        ['https://cnj.craigslist.org/','732-943-1909'],
        ['https://columbia.craigslist.org/','614-654-4810'],
        ['https://dallas.craigslist.org','214-382-0735'],
        ['https://denver.craigslist.org','720-583-8810'],
        ['https://houston.craigslist.org/','281-853-9054'],
        ['https://inlandempire.craigslist.org/','951-934-0167'],
        ['https://jacksonville.craigslist.org/','904-495-7764'],
        ['https://lasvegas.craigslist.org/','702-728-4280'],
        ['https://longisland.craigslist.org/','718-395-7860'],
        ['https://losangeles.craigslist.org/','323-900-0319'],
        ['https://miami.craigslist.org/','786-429-0170'],
        ['https://minneapolis.craigslist.org/','612-808-0271'],
        ['https://orangecounty.craigslist.org/','949-415-5991'],
        ['https://orlando.craigslist.org/','407-915-0560'],
        ['https://phoenix.craigslist.org/','480-470-7905'],
        ['https://pittsburgh.craigslist.org/','412-685-4101'],
        ['https://sacramento.craigslist.org/','916-571-0193'],
        ['https://seattle.craigslist.org/','206-258-6493'],
        ['https://tampa.craigslist.org/','813-513-9466']
    ]
elif campaign == 'flooring':
    citiesArray = [
        #['https://akroncanton.craigslist.org/','330-631-4628'],
        #['https://atlanta.craigslist.org','678-500-8943'],
        #['https://austin.craigslist.org','512-758-2192'],
        #['https://boise.craigslist.org/','208-501-8589'],
        #['https://chicago.craigslist.org','773-716-3623'],
        #['https://cincinnati.craigslist.org/','513-549-1957'],
        #['https://cleveland.craigslist.org/','216-415-7801'],
        #['https://cnj.craigslist.org/','201-942-4449'],
        #['https://cosprings.craigslist.org/','719-651-3561'],
        #['https://dallas.craigslist.org','469-802-0031'],
        #['https://denver.craigslist.org','720-897-4424'],
        #['https://detroit.craigslist.org','313-681-5066'],
        #['https://hartford.craigslist.org/','860-796-2919'],
        #['https://houston.craigslist.org/','832-426-3180'],
        #['https://inlandempire.craigslist.org','951-732-5399'],
        #['https://jacksonville.craigslist.org/','904-631-5614'],
        #['https://lasvegas.craigslist.org','702-800-0192'],
        #['https://losangeles.craigslist.org/','562-645-3961'],
        #['https://miami.craigslist.org/','786-454-2776'],
        #['https://minneapolis.craigslist.org','612-886-3177'],
        #['https://norfolk.craigslist.org/','757-383-7990'],
        #['https://orangecounty.craigslist.org','949-870-9907'],
        #['https://orlando.craigslist.org/','407-745-0079'],
        #['https://philadelphia.craigslist.org/','267-351-6658'],
        #['https://phoenix.craigslist.org','602-726-9678'],
        #['https://portland.craigslist.org','503-890-3075'],
        #['https://raleigh.craigslist.org/','984-664-0068'],
        #['https://sacramento.craigslist.org','916-668-4096'],
        #['https://sanantonio.craigslist.org','830-715-4476'],
        #['https://sandiego.craigslist.org','619-452-0011'],
        #['https://seattle.craigslist.org','360-602-2904'],
        #['https://sfbay.craigslist.org','415-795-2407'],
        #['https://stlouis.craigslist.org','314-696-6190'],
        #['https://tampa.craigslist.org/','813-906-0029']
    ]
elif campaign == 'locksmith':
    citiesArray = [

        ['https://lasvegas.craigslist.org','702-979-1541'],
        ['https://longisland.craigslist.org/','718-260-6897'],
        ['https://losangeles.craigslist.org/','323-629-4811'],
        ['https://miami.craigslist.org/','786-446-8051'],
        ['https://minneapolis.craigslist.org','612-260-8934'],
        ['https://norfolk.craigslist.org/','757-401-6327'],
        ['https://nyc.craigslist.org/','718-571-8783'],
        ['https://orangecounty.craigslist.org','949-438-5565'],
        ['https://orlando.craigslist.org/','407-456-7401'],
        ['https://philadelphia.craigslist.org/','610-624-2755'],
        ['https://phoenix.craigslist.org','602-883-2320'],
        ['https://pittsburgh.craigslist.org/','612-999-2141'],
        ['https://portland.craigslist.org','503-894-5685'],
        ['https://raleigh.craigslist.org/','919-816-2792'],
        ['https://richmond.craigslist.org/','804-201-4463'],
        ['https://sacramento.craigslist.org','916-382-8972'],
        ['https://sanantonio.craigslist.org','210-714-1454'],
        ['https://sandiego.craigslist.org','619-452-1038'],
        ['https://seattle.craigslist.org','206-981-3211'],
        ['https://sfbay.craigslist.org','415-582-4506'],
        ['https://stlouis.craigslist.org','314-287-5730'],
        ['https://tampa.craigslist.org/','813-639-8812'],
    ]


'''
askingPrice = ''
cardNum = '4246315203006950'
cardCv = '723'
cardMonth = '12'
cardYear = '19'
cardFirstName = 'Daniel'
cardLastName = 'Rusu'
cardAddress = '1117 huntington st'
cardCity = 'huntington beach'
cardState = 'CA'
cardPostal = '92648'
cardContactName = 'daniel rusu'
cardContactPhone = '9495310422'
zipCode = '98034'
