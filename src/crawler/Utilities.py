'''
Created on May 9, 2012

@author: Tyler, Nolan
'''

import re

class Utilities(object):
    
    def __init__(self):
        self.common_words = []
        s = """a
ability
able
about
about
above
above
absence
absolutely
academic
accept
access
accident
accompany
according
account
account
achieve
achievement
acid
acquire
across
act
act
action
active
activity
actual
actually
add
addition
additional
address
address
administration
admit
adopt
adult
advance
advantage
advice
advise
affair
affect
afford
afraid
after
after
afternoon
afterwards
again
against
age
agency
agent
ago
agree
agreement
ahead
aid
aim
aim
air
aircraft
all
all
allow
almost
alone
alone
along
along
already
alright
also
alternative
alternative
although
always
among
amongst
amount
an
analysis
ancient
and
animal
announce
annual
another
answer
answer
any
anybody
anyone
anything
anyway
apart
apparent
apparently
appeal
appeal
appear
appearance
application
apply
appoint
appointment
approach
approach
appropriate
approve
area
argue
argument
arise
arm
army
around
around
arrange
arrangement
arrive
art
article
artist
as
as
as
ask
aspect
assembly
assess
assessment
asset
associate
association
assume
assumption
at
atmosphere
attach
attack
attack
attempt
attempt
attend
attention
attitude
attract
attractive
audience
author
authority
available
average
avoid
award
award
aware
away
aye
baby
back
back
background
bad
bag
balance
ball
band
bank
bar
base
base
basic
basis
battle
be
bear
beat
beautiful
because
become
bed
bedroom
before
before
before
begin
beginning
behaviour
behind
belief
believe
belong
below
below
beneath
benefit
beside
best
better
between
beyond
big
bill
bind
bird
birth
bit
black
block
blood
bloody
blow
blue
board
boat
body
bone
book
border
both
both
bottle
bottom
box
boy
brain
branch
break
breath
bridge
brief
bright
bring
broad
brother
budget
build
building
burn
bus
business
busy
but
buy
by
cabinet
call
call
campaign
can
candidate
capable
capacity
capital
car
card
care
care
career
careful
carefully
carry
case
cash
cat
catch
category
cause
cause
cell
central
centre
century
certain
certainly
chain
chair
chairman
challenge
chance
change
change
channel
chapter
character
characteristic
charge
charge
cheap
check
chemical
chief
child
choice
choose
church
circle
circumstance
citizen
city
civil
claim
claim
class
clean
clear
clear
clearly
client
climb
close
close
close
closely
clothes
club
coal
code
coffee
cold
colleague
collect
collection
college
colour
combination
combine
come
comment
comment
commercial
commission
commit
commitment
committee
common
communication
community
company
compare
comparison
competition
complete
complete
completely
complex
component
computer
concentrate
concentration
concept
concern
concern
concerned
conclude
conclusion
condition
conduct
conference
confidence
confirm
conflict
congress
connect
connection
consequence
conservative
consider
considerable
consideration
consist
constant
construction
consumer
contact
contact
contain
content
context
continue
contract
contrast
contribute
contribution
control
control
convention
conversation
copy
corner
corporate
correct
cos
cost
cost
could
council
count
country
county
couple
course
court
cover
cover
create
creation
credit
crime
criminal
crisis
criterion
critical
criticism
cross
crowd
cry
cultural
culture
cup
current
currently
curriculum
customer
cut
cut
damage
damage
danger
dangerous
dark
data
date
date
daughter
day
dead
deal
deal
death
debate
debt
decade
decide
decision
declare
deep
deep
defence
defendant
define
definition
degree
deliver
demand
demand
democratic
demonstrate
deny
department
depend
deputy
derive
describe
description
design
design
desire
desk
despite
destroy
detail
detailed
determine
develop
development
device
die
difference
different
difficult
difficulty
dinner
direct
direct
direction
directly
director
disappear
discipline
discover
discuss
discussion
disease
display
display
distance
distinction
distribution
district
divide
division
do
doctor
document
dog
domestic
door
double
doubt
down
down
draw
drawing
dream
dress
dress
drink
drink
drive
drive
driver
drop
drug
dry
due
during
duty
each
ear
early
early
earn
earth
easily
east
easy
eat
economic
economy
edge
editor
education
educational
effect
effective
effectively
effort
egg
either
either
elderly
election
element
else
elsewhere
emerge
emphasis
employ
employee
employer
employment
empty
enable
encourage
end
end
enemy
energy
engine
engineering
enjoy
enough
enough
ensure
enter
enterprise
entire
entirely
entitle
entry
environment
environmental
equal
equally
equipment
error
escape
especially
essential
establish
establishment
estate
estimate
even
evening
event
eventually
ever
every
everybody
everyone
everything
evidence
exactly
examination
examine
example
excellent
except
exchange
executive
exercise
exercise
exhibition
exist
existence
existing
expect
expectation
expenditure
expense
expensive
experience
experience
experiment
expert
explain
explanation
explore
express
expression
extend
extent
external
extra
extremely
eye
face
face
facility
fact
factor
factory
fail
failure
fair
fairly
faith
fall
fall
familiar
family
famous
far
far
farm
farmer
fashion
fast
fast
father
favour
fear
fear
feature
fee
feel
feeling
female
few
few
field
fight
figure
file
fill
film
final
finally
finance
financial
find
finding
fine
finger
finish
fire
firm
first
fish
fit
fix
flat
flight
floor
flow
flower
fly
focus
follow
following
food
foot
football
for
for
force
force
foreign
forest
forget
form
form
formal
former
forward
foundation
free
freedom
frequently
fresh
friend
from
front
front
fruit
fuel
full
fully
function
fund
funny
further
future
future
gain
game
garden
gas
gate
gather
general
general
generally
generate
generation
gentleman
get
girl
give
glass
go
goal
god
gold
good
good
government
grant
grant
great
green
grey
ground
group
grow
growing
growth
guest
guide
gun
hair
half
half
hall
hand
hand
handle
hang
happen
happy
hard
hard
hardly
hate
have
he
head
head
health
hear
heart
heat
heavy
hell
help
help
hence
her
her
here
herself
hide
high
high
highly
hill
him
himself
his
his
historical
history
hit
hold
hole
holiday
home
home
hope
hope
horse
hospital
hot
hotel
hour
house
household
housing
how
however
huge
human
human
hurt
husband
i
idea
identify
if
ignore
illustrate
image
imagine
immediate
immediately
impact
implication
imply
importance
important
impose
impossible
impression
improve
improvement
in
is
incident
include
including
income
increase
increase
increased
increasingly
indeed
independent
index
indicate
individual
individual
industrial
industry
influence
influence
inform
information
initial
initiative
injury
inside
inside
insist
instance
instead
institute
institution
instruction
instrument
insurance
intend
intention
interest
interested
interesting
internal
international
interpretation
interview
into
introduce
introduction
investigate
investigation
investment
invite
involve
iron
island
issue
issue
it
item
its
itself
job
join
joint
journey
judge
judge
jump
just
justice
keep
key
key
kid
kill
kind
king
kitchen
knee
know
knowledge
labour
labour
lack
lady
land
language
large
largely
last
last
late
late
later
latter
laugh
launch
law
lawyer
lay
lead
lead
leader
leadership
leading
leaf
league
lean
learn
least
leave
left
leg
legal
legislation
length
less
less
let
letter
level
liability
liberal
library
lie
life
lift
light
light
like
like
likely
limit
limit
limited
line
link
link
lip
list
listen
literature
little
little
little
live
living
loan
local
location
long
long
look
look
lord
lose
loss
lot
love
love
lovely
low
lunch
machine
magazine
main
mainly
maintain
major
majority
make
male
male
man
manage
management
manager
manner
many
map
mark
mark
market
market
marriage
married
marry
mass
master
match
match
material
matter
matter
may
may
maybe
me
meal
mean
meaning
means
meanwhile
measure
measure
mechanism
media
medical
meet
meeting
member
membership
memory
mental
mention
merely
message
metal
method
middle
might
mile
military
milk
mind
mind
mine
minister
ministry
minute
miss
mistake
model
modern
module
moment
money
month
more
more
morning
most
most
mother
motion
motor
mountain
mouth
move
move
movement
much
much
murder
museum
music
must
my
myself
name
name
narrow
nation
national
natural
nature
near
nearly
necessarily
necessary
neck
need
need
negotiation
neighbour
neither
network
never
nevertheless
new
news
newspaper
next
next
nice
night
no
no
no
no-one
nobody
nod
noise
none
nor
normal
normally
north
northern
nose
not
note
note
nothing
notice
notice
notion
now
nuclear
number
nurse
object
objective
observation
observe
obtain
obvious
obviously
occasion
occur
odd
of
off
off
offence
offer
offer
office
officer
official
official
often
oil
okay
old
on
on
once
once
one
only
only
onto
open
open
operate
operation
opinion
opportunity
opposition
option
or
order
order
ordinary
organisation
organise
organization
origin
original
other
other
other
otherwise
ought
our
ourselves
out
outcome
output
outside
outside
over
over
overall
own
own
owner
package
page
pain
paint
painting
pair
panel
paper
parent
park
parliament
part
particular
particularly
partly
partner
party
pass
passage
past
past
past
path
patient
pattern
pay
pay
payment
peace
pension
people
per
percent
perfect
perform
performance
perhaps
period
permanent
person
personal
persuade
phase
phone
photograph
physical
pick
picture
piece
place
place
plan
plan
planning
plant
plastic
plate
play
play
player
please
pleasure
plenty
plus
pocket
point
point
police
policy
political
politics
pool
poor
popular
population
position
positive
possibility
possible
possibly
post
potential
potential
pound
power
powerful
practical
practice
prefer
prepare
presence
present
present
present
president
press
press
pressure
pretty
prevent
previous
previously
price
primary
prime
principle
priority
prison
prisoner
private
probably
problem
procedure
process
produce
product
production
professional
profit
program
programme
progress
project
promise
promote
proper
properly
property
proportion
propose
proposal
prospect
protect
protection
prove
provide
provided
provision
pub
public
public
publication
publish
pull
pupil
purpose
push
put
quality
quarter
question
question
quick
quickly
quiet
quite
race
radio
railway
rain
raise
range
rapidly
rare
rate
rather
reach
reaction
read
reader
reading
ready
real
realise
reality
realize
really
reason
reasonable
recall
receive
recent
recently
recognise
recognition
recognize
recommend
record
record
recover
red
reduce
reduction
refer
reference
reflect
reform
refuse
regard
region
regional
regular
regulation
reject
relate
relation
relationship
relative
relatively
release
release
relevant
relief
religion
religious
rely
remain
remember
remind
remove
repeat
replace
reply
report
report
represent
representation
representative
request
require
requirement
research
resource
respect
respond
response
responsibility
responsible
rest
rest
restaurant
result
result
retain
return
return
reveal
revenue
review
revolution
rich
ride
right
right
right
ring
ring
rise
rise
risk
river
road
rock
role
roll
roof
room
round
round
route
row
royal
rule
run
run
rural
safe
safety
sale
same
sample
satisfy
save
say
scale
scene
scheme
school
science
scientific
scientist
score
screen
sea
search
search
season
seat
second
secondary
secretary
section
sector
secure
security
see
seek
seem
select
selection
sell
send
senior
sense
sentence
separate
separate
sequence
series
serious
seriously
servant
serve
service
session
set
set
settle
settlement
several
severe
sex
sexual
shake
shall
shape
share
share
she
sheet
ship
shoe
shoot
shop
short
shot
should
shoulder
shout
show
show
shut
side
sight
sign
sign
signal
significance
significant
silence
similar
simple
simply
since
since
sing
single
sir
sister
sit
site
situation
size
skill
skin
sky
sleep
slightly
slip
slow
slowly
small
smile
smile
so
so
social
society
soft
software
soil
soldier
solicitor
solution
some
somebody
someone
something
sometimes
somewhat
somewhere
son
song
soon
sorry
sort
sound
sound
source
south
southern
space
speak
speaker
special
species
specific
speech
speed
spend
spirit
sport
spot
spread
spring
staff
stage
stand
standard
standard
star
star
start
start
state
state
statement
station
status
stay
steal
step
step
stick
still
stock
stone
stop
store
story
straight
strange
strategy
street
strength
strike
strike
strong
strongly
structure
student
studio
study
study
stuff
style
subject
substantial
succeed
success
successful
such
suddenly
suffer
sufficient
suggest
suggestion
suitable
sum
summer
sun
supply
supply
support
support
suppose
sure
surely
surface
surprise
surround
survey
survive
switch
system
table
take
talk
talk
tall
tape
target
task
tax
tea
teach
teacher
teaching
team
tear
technical
technique
technology
telephone
television
tell
temperature
tend
term
terms
terrible
test
test
text
than
thank
thanks
that
that
the
theatre
their
them
theme
themselves
then
theory
there
there
therefore
these
they
thin
thing
think
this
those
though
though
thought
threat
threaten
through
through
throughout
throw
thus
ticket
time
tiny
title
to
to
to
today
together
tomorrow
tone
tonight
too
tool
tooth
top
top
total
total
totally
touch
touch
tour
towards
town
track
trade
tradition
traditional
traffic
train
train
training
transfer
transfer
transport
travel
treat
treatment
treaty
tree
trend
trial
trip
troop
trouble
true
trust
truth
try
turn
turn
twice
type
typical
unable
under
under
understand
understanding
undertake
unemployment
unfortunately
union
unit
united
university
unless
unlikely
until
until
up
up
upon
upper
urban
us
use
use
used
used
useful
user
usual
usually
value
variation
variety
various
vary
vast
vehicle
version
very
very
via
victim
victory
video
view
village
violence
vision
visit
visit
visitor
vital
voice
volume
vote
vote
wage
wait
walk
walk
wall
want
war
warm
warn
wash
watch
water
wave
way
we
weak
weapon
wear
weather
week
weekend
weight
welcome
welfare
well
well
west
western
what
whatever
when
when
where
where
whereas
whether
which
while
while
whilst
white
who
whole
whole
whom
whose
why
wide
widely
wife
wild
will
will
win
wind
window
wine
wing
winner
winter
wish
with
withdraw
within
without
woman
wonder
wonderful
wood
word
work
work
worker
working
works
world
worry
worth
would
write
writer
writing
wrong
yard
yeah
year
yes
yesterday
yet
you
young
your
yourself
youth"""
        self.common_words = s.split("\n")
    
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Utilities, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    
    """
    Converts text input into a list of words.
    This function assume all text has already been converted to proper ASCII encoding.
    """
    def word_list(self, text, ignore_case = True):    
        # Changes all text to lowercase.
        if ignore_case:
            text = text.lower()
    
        # Removes ASCII apostrophes from the text.
        text = text.replace("'", "")
        
        # Removes commas from the text. We assume that all text
        # is formatted correctly in that there are no typographic errors.
        text = text.replace(",", "")
        
        # Replaces all non-word character with spaces to represent word boundaries.
        rx = re.compile("[^\w ]")
        text = rx.sub(" ", text)    
        
        # Splits words that are divided by spaces.
        text = text.split()
        
        # If any "empty words" have been manufactured by previous processes, drop them.
        text = [x for x in text if len(x) > 1]
        return text
    
    """
    Takes a string of text and returns list of unique words and their frequencies.
    """
    def word_frequencies(self, text):
        words = self.word_list(text)
        unique_words = set(words)
        return sorted([(words.count(word), word) for word in unique_words])
    
    """
    Takes a list of word frequencies and returns up to numWords of the most
    frequently used words that do no belong to commonWords. Returns
    an empty list if numWords <= 0 or if all of the words in wordCounts
    are found in commonWords.
    """
    def top_k_unique_words(self, word_counts, num_words, common_words):
        result = []
        if num_words > 0:
            count = 0
            while (count < num_words) and word_counts:
                word = word_counts.pop()[1]
                if not (word in common_words):
                    result.append(word)
                    count += 1
        return result


#if __name__ == '__main__':
#    s1=Utilities()
#    s2=Utilities()
#    if(id(s1)==id(s2)):
#        print "Same"
#    else:
#        print "Different"